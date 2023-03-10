#!/usr/bin/env python
'''
Calculate your income taxes
'''
import sys

# Set tax rates
RATE1 = 0.10
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = RATE1_SINGLE_LIMIT * 2# double it
# Take input
income = input('Please enter your income: ')

# TODO: Validate input
if type(income) == float or type(income) == int:
    print('Valid input')
else:
    print('Invalid input')
    print("Please enter a decimal value ")
    sys.exit(2)  # exit the program now. != 0 means error
# Validate input
if MARITAL_STATUS != 's' or MARITAL_STATUS != 'm':
    print('Invalid input')
    print("Please enter 's' for single or 'm' for married: ")
    sys.exit(1)  # exit the program now. 1= 0 means error

# Compute taxes
tax1 = 0.0 # first rate
tax2 = 0.0 # second rate

if marital_status == 's':
    if income <= RATE1_SINGLE_LIMIT:
        tax1 = RATE1 * income 
    else:
        tax1 = RATE1 * RATE1_SINGLE_LIMIT
        tax2 = RATE2 * (income - RATE1_SINGLE_LIMIT)
else:                                               # 'm' case
    if income <= RATE1_MARRIED_LIMIT:
        tax1 = RATE1 * income
    else:
        tax1 = RATE1 * RATE1_MARRIED_LIMIT
        tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)
# Calculate totals taxes
total_taxes = tax1 + tax2
print(f'Your total taxes are {total_taxes}')

sys.exit(0)  # 0 means no error