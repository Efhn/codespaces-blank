#!/usr/bin/env python
'''
Create a file that ask the user to enter 5 integers (age).
Store information in a `list`, then, print all values
'''

num_ages = int(input('How many integers do you want to capture:'))
# loop to take user input
# ages = [] # empty list
for index in range(num_ages):
    ages = [] # empty list
    age = int(input('Enter your age'))
    # Save values in a list
    ages.append(age)

# Loop to print input
for age in ages:
    print(age)

# TODO: Print the average age
total = 0
for age in ages:
    total += age

print(f'Total of ages is {total}')
print(f'Average {total/len(ages)}')
print(f'Max age {max(ages)}')
print(f'Minimum age {min(ages)}')