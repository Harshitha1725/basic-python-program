# Number Guessing Game
# Created by Harshitha HM

import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

number = random.randint(1, 10)

try:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Congratulations! You guessed it right!")
    else:
        print(f"❌ Oops! The correct number was {number}.")

except ValueError:
    print("⚠️ Please enter a valid number between 1 and 10.")