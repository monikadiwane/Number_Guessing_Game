#Number Guessing Game Objectives:
from art import logo
import random
# Include an ASCII art logo.
def guess():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    level = input("Choose the difficulty level. Type 'easy' or 'hard': ")
    if level == 'hard':
        attempt = 5
    else:
        attempt = 10

    number = random.randint(1,100)
    #print(number)
# Allow the player to submit a guess for a number between 1 and 100.
    while attempt != 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Hurray!!! You guess it right.")
            break
        elif guess > number:
            print("Too high.")    
        else:
            print("Too low.")

        attempt -=1

        if attempt == 0:
            print("You have run out of guess. You Lose.")
        else:
            print("Guess again")
            
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

guess()
