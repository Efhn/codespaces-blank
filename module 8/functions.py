#!/usr/bin/env python
"""
Module documentation
"""
import sys


def waldo():
    print('Hello to WSU')


def who_are_you(person):
    if callable(person):
        person() # execute/call the function
    else:
        print(f'Hi {person}')


def main():
    """
    Main Driver
    """
    waldo()
    # Pass function as param
    # DO NOT use parenthesis
    who_are_you(waldo)
    who_are_you('Hugo')
    who_are_you([1,2,3])
    who_are_you(who_are_you)



if __name__ == '__main__':
    main()
    sys.exit(0)