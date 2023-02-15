#!/usr/bin/env python
"""
Guess a random number between 0 and 100. Provide some hints to the user
"""
from random import randint 

NUMBER = randint(0,101)
total = 5
while True:
    if total == 0:
        break  # use all your tries
    guess = int(input('Enter your guess from 0 to 100, You have {total} tries: '))
    # Provide a hint
    if guess > NUMBER:
        print('Go lower')
    elif guess < NUMBER:
        print('Go Higher')
    else:
        # guess == NUMBER
        break   # exit the loop
    total = total - 1
        

print(f'You got it. Your found the guess number: {total}')
