# box_shooter.py
import pygame
import random
import math
import sys

# --- Game Config Settings
WIDTH, HEIGHT = 400, 400
BOX_SIZE = 20

# --- Speed Settings ---
WHITE_SPEED = 20
GREEN_SPEED = 5
RED_SPEED = 2
ORANGE_SPEED = 4

# --- Enemy Spawning Settings ---
# Enemy spawn timing (influenced by SPAWN_RATE)
# 1.0 = normal speed, <1 = faster spawns, >1 = slower spawns
SPAWN_RATE = 0.1

# Base spawn interval in milliseconds (scaled by SPAWN_RATE)
SPAWN_MIN_MS = int(500 * SPAWN_RATE)
SPAWN_MAX_MS = int(2500 * SPAWN_RATE)

# --- Shooting settings ---
GREEN_SHOOT_COOLDOWN = 0   # milliseconds between shots
ORANGE_SHOOT_COOLDOWN = 0  # milliseconds between shots

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
ORANGE = (255, 140, 0)

# --- Start of the actual code (no longer just settings) ---

class Player:
    def __init__(self, x=0, y=0):
        self.rect = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)

    def move(self, dx, dy):
        self.rect.x = max(0, min(WIDTH - BOX_SIZE, self.rect.x + dx))
        self.rect.y = max(0, min(HEIGHT - BOX_SIZE, self.rect.y + dy))

    def draw(self, surf):
        pygame.draw.rect(surf, WHITE, self.rect)


class Enemy:
    def __init__(self, x):
        self.rect = pygame.Rect(x, 0, BOX_SIZE, BOX_SIZE)
        self.speed = RED_SPEED

    def update(self):
        self.rect.y += self.speed

    def draw(self, surf):
        pygame.draw.rect(surf, RED, self.rect)


class GreenProjectile:
    # simple upward projectile
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
        self.speed = GREEN_SPEED

    def update(self):
        self.rect.y -= self.speed

    def offscreen(self):
        return self.rect.bottom < 0

    def draw(self, surf):
        pygame.draw.rect(surf, GREEN, self.rect)


class OrangeProjectile:
    # homing projectile: chases the closest red enemy
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)
        self.speed = ORANGE_SPEED

    def update(self, enemies):
        # Find closest enemy
        if not enemies:
            # just go up if no enemies (or stay still)
            self.rect.y -= self.speed
            return

        closest = min(enemies, key=lambda e: math.hypot(e.rect.centerx - self.rect.centerx,
                                                         e.rect.centery - self.rect.centery))
        tx, ty = closest.rect.centerx, closest.rect.centery
        dx = tx - self.rect.centerx
        dy = ty - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist == 0:
            return
        # normalize and step by speed
        nx = dx / dist
        ny = dy / dist
        self.rect.x += int(round(nx * self.speed))
        self.rect.y += int(round(ny * self.speed))

    def offscreen(self):
        return (self.rect.right < 0 or self.rect.left > WIDTH or
                self.rect.bottom < 0 or self.rect.top > HEIGHT)

    def draw(self, surf):
        pygame.draw.rect(surf, ORANGE, self.rect)


def spawn_enemy():
    x = random.randint(0, WIDTH - BOX_SIZE)
    return Enemy(x)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Box Shooter - Python (Pygame)")
    clock = pygame.time.Clock()
    FONT = pygame.font.SysFont(None, 18)
    player = Player(0, 0)  # same starting place as the JS (top-left)
    enemies = []
    greens = []
    oranges = []
    global HEALTH
    HEALTH = 100

    next_spawn_time = pygame.time.get_ticks() + random.randint(SPAWN_MIN_MS, SPAWN_MAX_MS)

    # track when last shot was fired (for cooldowns)
    last_green_shot = 0
    last_orange_shot = 0
    
    running = True
    while running:
        dt = clock.tick(60)  # 60 FPS target
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # keydown events for shooting (space and enter)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    g = GreenProjectile(player.rect.x, player.rect.y)
                    greens.append(g)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    o = OrangeProjectile(player.rect.x, player.rect.y)
                    oranges.append(o)


        # key held down for movement
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]:
            dx -= WHITE_SPEED
        elif keys[pygame.K_a]:
            dx -= WHITE_SPEED
        if keys[pygame.K_RIGHT]:
            dx += WHITE_SPEED
        elif keys[pygame.K_d]:
            dx += WHITE_SPEED
        if keys[pygame.K_UP]:
            dy -= WHITE_SPEED
        elif keys[pygame.K_w]:
            dy -= WHITE_SPEED
        if keys[pygame.K_DOWN]:
            dy += WHITE_SPEED
        elif keys[pygame.K_s]:
            dy += WHITE_SPEED
        player.move(dx, dy)
        
        # continuous shooting (hold to fire)
        now = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and now - last_green_shot >= GREEN_SHOOT_COOLDOWN:
            g = GreenProjectile(player.rect.x, player.rect.y)
            greens.append(g)
            last_green_shot = now
        
        if (keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and now - last_orange_shot >= ORANGE_SHOOT_COOLDOWN:
            o = OrangeProjectile(player.rect.x, player.rect.y)
            oranges.append(o)
            last_orange_shot = now

        if HEALTH < 1:
            print("You ran out of health.")
            break
            return "Player died"

        # Update enemies
        for e in enemies[:]:
            e.update()
            # remove enemy if reaches bottom
            if e.rect.top > HEIGHT:
                enemies.remove(e)
                HEALTH -= 1
            else:
                # check collision with oranges (orange removes red)
                for o in oranges[:]:
                    if e.rect.colliderect(o.rect):
                        if e in enemies:
                            enemies.remove(e)
                        if o in oranges:
                            oranges.remove(o)
                        break

        # Update green projectiles
        for g in greens[:]:
            g.update()
            if g.offscreen():
                greens.remove(g)
                continue
            # check collision with enemies
            for e in enemies[:]:
                if g.rect.colliderect(e.rect):
                    if e in enemies:
                        enemies.remove(e)
                    if g in greens:
                        greens.remove(g)
                    break

        # Update orange projectiles (homing)
        for o in oranges[:]:
            o.update(enemies)
            if o.offscreen():
                oranges.remove(o)
                continue
            # collision with enemies also handled above (in enemies update),
            # but check here too in case of same-frame collisions
            for e in enemies[:]:
                if o.rect.colliderect(e.rect):
                    if e in enemies:
                        enemies.remove(e)
                    if o in oranges:
                        oranges.remove(o)
                    break

        # spawn enemies at randomized intervals (like setTimeout with random)
        now = pygame.time.get_ticks()
        if now >= next_spawn_time:
            enemies.append(spawn_enemy())
            next_spawn_time = now + random.randint(SPAWN_MIN_MS, SPAWN_MAX_MS)

        # draw
        screen.fill(BLACK)
        player.draw(screen)
        for e in enemies:
            e.draw(screen)
        for g in greens:
            g.draw(screen)
        for o in oranges:
            o.draw(screen)

        # small HUD (optional): counts
        hud = FONT.render(f"Enemies: {len(enemies)}  Greens: {len(greens)}  Oranges: {len(oranges)} Health: {HEALTH}", True, (200, 200, 200))
        screen.blit(hud, (6, HEIGHT - 20))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def info(option=3, challenge=1):
    if option == 1 or option == 3
        print("A box shooter game where you play as")
        print("the white box and shoot down the red ")
        print("boxes to prevent them from reaching ")
        print("the bottom of the pygame window.")
    if option == 


if __name__ == "__main__":
    main()
