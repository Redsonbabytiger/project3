import random
def computerAsksUser():
    randNum = random.randint(1, 100)
    guess = 0
    guessNum = 0
    while guess != randNum:
        guess = int(input("Guess the number I'm thinking of: "))
        guessNum += 1
        if guess > randNum:
            print("Your guess is too high, try again.")
        elif guess < randNum:
            print("Your guess is too low, try again.")
        elif guess == randNum:
            print("")
            print("Congratulations! You guessed it!")
            print("And it only took you", guessNum, "tries.")


def computerGuesses():
    guessNum = int(input("What number should the computer guess? "))
    tryNum = 0
    computerGuess = random.randint(1, 100)
    while computerGuess != guessNum:
        computerGuess = random.randint(1, 100)
        tryNum += 1
        if computerGuess > guessNum:
            print("Computer guessed", computerGuess, "Which was too high.")
        elif computerGuess < guessNum:
            print("Computer guessed", computerGuess, "Which was too low.")
        elif computerGuess == guessNum:
            print("")
            print("Congratulations! The computer guessed it!")
            print("The number was", guessNum)
            print("And it only took the computer", tryNum, "tries.")

def computerGuessesNoOutput():
    guessNum = int(input("What number should the computer guess? "))
    maxNum = 100
    if guessNum > 100:
        maxNum = guessNum
    tryNum = 0
    computerGuess = random.randint(1, maxNum)
    while computerGuess != guessNum:
        computerGuess = random.randint(1, maxNum)
        tryNum += 1
        if computerGuess == guessNum:
            print("")
            print("Congratulations! The computer guessed it!")
            print("The number was", guessNum)
            print("And it only took the computer", tryNum, "tries.")
        else:
            print(computerGuess)
        if tryNum > 300:
            print("I give up, I don't know what it is.")
            break
            break

def userAsksComputer():
    turns=0
    bottom=0
    top=101
    num=int(input("Please enter a number from 1-100 & the computer will guess it: "))
    guess=random.randint(1,100)
    print("Computer guesses "+str(guess))
    while True:
        while True:
            horl=input("Is the your number Higher or Lower or did the computer guess correct(say You Guessed It)? ")
            if guess<num and horl!="Higher" or guess>num and horl!="Lower" or num==guess and horl!="You Guessed It":
                print("Try again")
            else:
                break
        turns+=1
        if horl=="Higher":
            bottom=guess+1
            guess=random.randint(bottom,top)
        if horl=="Lower":
            top=guess-1
            guess=random.randint(bottom,top)
        print("Computer guesses "+str(guess))
        if horl=="You Guessed It":
            break
    print("Congrats! It took the computer " + str(turns) + " guesses.")

