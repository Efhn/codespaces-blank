#!/usr/bin/env python
"""
Create a passwrod generator
"""
import sys
import string
import random

def generate_password(length, complexity):
    if length < 8:
        return 'invalid length'
    # Generate password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    password = ''
    # Basic: lower + upper + digits
    if complexity == 'basic':
        pass
    # Intermediate: basic + special
    elif complexity == 'intermediate':
        pass
    # Advanced: Intermediate + '!@#$%^&()*'
    elif complexity == 'advanced':
        pass
    else:
        password = 'Invalid complexity'

    return password


def main():
    """
    Main Driver
    """
    length = input('Enter the password length (min 8 chars) ')
    complexity = input('Complexity level: basic, intermediate, advanced')
    password = generate_password(length, complexity)
    print(password)


if __name__ == '__main__':
    main()
    sys.exit(0)