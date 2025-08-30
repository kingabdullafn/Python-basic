import random

options = ["Rock","Paper","Scissors"]
user_choice = input("choose Rock, Paper, or  Scissors: ")
Computer_choice = random.choice(options)
print("Computer chose:", Computer_choice)

if user_choice == Computer_choice:
    print("It's a tie"!)