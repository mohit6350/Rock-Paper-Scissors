import sys
import random

print("".ljust(30,"="))
user_choice = int(input(" Enter 1 for 💎 ROCK \n Enter 2 for 🧻 PAPER \n Enter 3 for ✂  SCISSORS \n\n Please choose : "))
print("\n")
computer_choice = int(random.choice("123"))
print(f" You choose    : {user_choice}")
print(f" Python choose : {computer_choice}")

if user_choice == 1 and computer_choice == 3:
    print(" \n🎉You win !")
elif user_choice == 2 and computer_choice == 1:
    print(" \n🎉You win !")
elif user_choice == 3 and computer_choice == 2:
    print(" \n🎉You win !")
elif user_choice == computer_choice:
    print(" \n😱 It's a Tie !")
else:
    print(" \n🐍 Python wins !\n")
    
print("".ljust(30,"="))