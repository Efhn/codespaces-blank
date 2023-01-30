#!/usr/bin/env python
'''
Create a file that ask the user to enter 5 integers (age).
Store information in a `list`, then, print all values
'''

# TODO: loop to take user input
ages = [] # empty list
for index in range(5):
    age = int(input('Enter your age'))
    # TODO: Save values in a list
    ages.append(age)

# TODO: Loop to print input
for age in ages:
    print(age)

# TODO: Print the average age
