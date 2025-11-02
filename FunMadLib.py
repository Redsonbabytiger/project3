# Mad Libs: The Adventure of a Boy and a Girl

# Gather user inputs
boy_name = input("Enter a boy's name: ")
girl_name = input("Enter a girl's name: ")
place = input("Enter a noun for a place (e.g., forest, castle, city): ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
object1 = input("Enter a noun for an object: ")
object2 = input("Enter another noun for an object: ")
creature = input("Enter a noun for a creature (real or imaginary): ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")
emotion = input("Enter an adjective describing an emotion: ")

# Build the story
story = f"""
This is the story of {boy_name} and {girl_name}, two best friends who lived near a {adjective1} {place}.
One day, they decided to explore the {place}, bringing only a {object1} and a {object2} with them.
At first, everything seemed {adjective2}, and they laughed as they {verb1} down the winding paths.

But soon, the air grew {adjective3}, and out of the shadows appeared a giant {creature}.
The creature began to {verb2} toward them, shaking the ground with every step.
{boy_name} wanted to run, but {girl_name} whispered, “If we stay calm, maybe we can {verb3} our way out of this.”

Together, they held tightly onto their {object1} and {object2}, standing side by side.
The {creature} stopped, tilted its head, and let out a sound that was half a roar, half a laugh.
To their surprise, the creature wasn’t angry—it was just {emotion} and lonely.

In that moment, {boy_name} and {girl_name} realized that sometimes the scariest things just need a friend.
So they invited the {creature} to join them on their adventures.
From then on, the {adjective2} {place} wasn’t a place of fear, but a home for the greatest friendship they ever discovered.
"""

# Print the story
print(story)