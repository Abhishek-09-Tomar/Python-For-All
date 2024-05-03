"""
Problem Statement:
Make a program that guesses the number between 1 to 100 in 10 attempts and they run until you think the correct number.
"""

import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. You have 10 attempts to guess it.")

    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    if guess != number:
        print(f"Sorry, you have run out of attempts. The number was {number}.")

guess_number()
