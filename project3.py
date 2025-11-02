import random
import MadLib
import HighLowGame
import box_shooter
choice = "6"
print("Welcome to the My CS Python Project (First python project)")

while choice != "0":
    print("0) Quit")
    print("1) MadLib Story Making")
    print("2) High/Low Game")
    print("3) Box Shooter Game")
    print("4) Rock Paper Scissors")
    print("5) Tic-Tac-Toe")
    choice = input("Enter the number of the option you want: ")

    if choice == "0":
        print("Quitting...")
    elif choice == "1":
        MadLib.main()
    elif choice == "2":
        HighLowGame.userAsksComputer()
    elif choice == "3":
        box_shooter.main()
    elif choice == "4":
        rps = input("Rock, paper, or scissors? ").lower()
        choices = ["rock", "paper", "scissors"]
        if rps in choices:
            computerchoice = random.choice(choices)
            if rps == computerchoice:
                print("tie!")
            elif rps == "rock" and computerchoice == "scissors":
                print("You Win!")
            elif rps == "rock" and computerchoice == "paper":
                print("You lose!")
            elif rps == "paper" and computerchoice == "rock":
                print("You win!")
            elif rps == "paper" and computerchoice == "scissors":
                print("You lose!")
            elif rps == "scissors" and computerchoice == "paper":
                print("You win!")
            elif rps == "scissors" and computerchoice == "rock":
                print("You lose!")
            else:
                print("Something went wrong.")
        else:
            print("That's not one of the options.")
    elif choice == "5":
        pass
    else:
        print("That's not one of the options!")