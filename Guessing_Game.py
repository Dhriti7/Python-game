'''
This is a Guessing Game.
Input: Any number between 1 to 100
Output: Count of attepts to guess the number
Created By: Dhritiman Mukherjee
Date of Creation: 26-JAN-2020
'''
import random

'''importing random module to get a random number between 1 to 100'''

jackpot=random.randint(1,100)
guess=int(input("Let's Guess a number between 1 to 100: "))
counter=1
while guess!=jackpot:
    counter += 1
    if guess>jackpot:
        print("Guess lower")
        guess=int(input("Guess Again: "))
    else:
        print("Guess higher")
        guess=int(input("Guess Again: "))
print("Correct Guess in ",counter," attempts")
