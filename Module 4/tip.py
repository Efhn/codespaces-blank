#!/usr/bin/env python
"""
Compute the tip based on dinner's level of satisfaction
"""
# Read user input
import sys

print('Please use the following scale')
print('\t 1: Totally satisfied')
print('\t 2: Satisfied')
print('\t 3: Dissatisfied')
# TODO: Validate the input
satisfaction = input('What was your level of satisfaction? ')
if satisfaction == '1' or satisfaction == '2' or satisfaction == '3':
    pass
else:
    print('Invalid choice')
    sys.exit(1)

# TODO: Capture the bill
amount = float(input('How much was your bill? '))

# TODO: Read user input
if satisfaction == 1:
    # If satisfaction is 1, then 20% tip
    tip = amount * 0.20
    SATISFACTION_MESSAGE = 'very satisfied'
    pass
elif satisfaction == 2:
    # If satisfaction is 2, then 15% tip
    tip = amount * 0.15
    SATISFACTION_MESSAGE = 'satisfied'
    pass
else:   
    # If satisfaction is 3, then 10% tip
    tip = amount * 0.10
    SATISFACTION_MESSAGE = 'dissatisfied'
    pass

# TODO: Display the result
print(f'Because you were {SATISFACTION_MESSAGE}, your tip should be ${tip:.2f}')
