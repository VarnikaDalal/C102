import random

user_wins = 0
comp_wins = 0

options = ["Rock", "Paper", "Scissors", "Q"]

while True:
    print("Welcome to the game of Rock, Paper, Scissors!!")
    user_input = input("Please choose Rock/Paper/Scissors or Q to quit: ")

    if user_input == "Q":
        break

    if user_input not in options:
        user_input = input("Please choose Rock/Paper/Scissors or Q to quit: ")

    random_no = random.randint(0,2)
    comp_pick = options[random_no]
    print("Computer picked " + comp_pick + ".")

    if user_input == "Rock" and comp_pick ==  "Scissors":
        print("You Win!!")
        user_wins += 1

    elif user_input == "Paper" and comp_pick ==  "Rock":
        print("You Win!!")
        user_wins += 1

    elif user_input == "Scissors" and comp_pick ==  "Paper":
        print("You Win!!")
        user_wins += 1

    elif user_input == "Rock" and comp_pick ==  "Rock":
        print("It's a Draw")

    elif user_input == "Paper" and comp_pick ==  "Paper":
        print("It's a Draw")

    elif user_input == "Scissors" and comp_pick ==  "Scissors":
        print("It's a Draw")

    else:
        print("You Lost, Better luck next time")
        comp_wins += 1

print("You won", user_wins, "times.")
print("Computer won", comp_wins, "times.")



