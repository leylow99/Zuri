import random

input("Welcome to rock, Paper, Scissors! Press Enter to start: ")

user_score = 0
cpu_score = 0


print()

while True:
    user_choice = input("Rock, Paper, or Scissors? ").lower()
    while user_choice != "rock" and user_choice != "scissors" and user_choice != "rock":
        user_choice = input("invalid input please try again: ").lower()

    random_num = random.randint(0, 2)
    if random_num == 0:
        cpu_choice = "rock"
    elif random_num == 1:
        cpu_choice = "paper"
    elif random_num == 2:
        cpu_choice = "scissors"

    print("your choice is: ", user_choice)
    print("computer's choice is: ", cpu_choice)
    print()

    if user_choice == "rock":
        if cpu_choice == "rock":
            print("its a tie")
        elif cpu_choice == "paper":
            print("you lose")
            cpu_score += 1
        elif cpu_choice == "scissors":
            print("you wn")
            user_score += 1
    elif user_choice == "paper":
        if cpu_choice == "paper":
            print("its a tie")
        elif cpu_choice == "scissors":
            print("you lose")
            cpu_score += 1
        elif cpu_choice == "rock":
            print("you win")
            user_score += 1
    elif user_choice == "scissors":
        if cpu_choice == "scissors":
            print("its a tie")
        elif cpu_choice == "rock":
            print("you lose")
            cpu_score += 1
        elif cpu_choice == "paper":
            print("you win")
            user_score += 1

    print("you have", user_score, "wins")
    print("The computer has", cpu_score, "wins")
    print()

    repeat = input("Play again (y/n) ").lower()
    while repeat != "n" and repeat != "yes":
        repeat = input("invalid input please try again: ").lower()

    if repeat == "n":
        break
