#!/usr/bin/env python
"""
Module documentation for scoping. Local versus global variables
"""
import sys

count = 0


def show_count():
    """Print current count
    """
    print(f'Count = {count}')


def set_count(num):
    """Set the global count number

    Args:
        num (int): new value
    """
    # count = num # this is a LOCAL variable
    # To access the global variable
    global count  # link to global
    count = num


def main():
    """
    Main Driver
    """
    show_count()
    set_count(9)
    show_count()

if __name__ == '__main__':
    main()
    sys.exit(0)