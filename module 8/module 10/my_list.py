"""
Learn more List options
"""
import sys


def main():
    """
    Main Driver
    """
    numbers = [33, 22, 55, 4, 1, -9, 4, 0]
    print(numbers)
    # Make a full slice
    full = number[:] # your own copy in memory
    print(full)
    print(f'Same? {numbers is full}')
    
    # Make a copy
    numbers = [33, 22, 55, 4, 1, -9, 4, 0]
    new_numbers = numbers # Share