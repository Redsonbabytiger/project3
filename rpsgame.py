def game():
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