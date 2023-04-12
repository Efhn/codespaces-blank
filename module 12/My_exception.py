#!/usr/bin/env python
"""
Module documentation for exceptions
"""
import sys


def convert(s):
    """Convert input parameter to an integer

    Args:
    s (string): string to convert

    Returns
    """
    try:
        int_s = int(s)
    except ValueError:
        int_s = -1
    return int_s


def main():
    """
    Main Driver
    """
    pass

