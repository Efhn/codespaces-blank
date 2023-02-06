#!/usr/bin/env python
'''
Calculate your income taxes
'''
# Set tax rates
RATE1 = 0.10
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = RATE1_SINGLE_LIMIT * 2# double it
# Take input
income = float(input('Please enter your income'))
marital_status = input('Please enter s for single pr m for married')
# Compute taxes
tax1 = 0.0
tax2 = 0.0

if marital_status == 's':
    # TODO: Set rules
    if income <= RATE1_SINGLE_LIMIT:
        tax1 = RATE1 * income 
else:
    if icome <= RATE1_MARRIED_LIMIT
        tax1 = RATE1 * income
        else:
            pass  # TODO
# Calculate totals taxes
total_taxes = tax1 + tax2
print(f'Your total taxes are {total_taxes}')