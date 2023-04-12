#!/usr/bin/env python
"""
An air traveling system
"""
import sys


class Flight:
    # Initializer or constructor
    def __init__(self, number):
        # Validate the input, format: AA###
        # 1) First two are alpha
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in {number}')
        # 2) First two are Uppercase
        if not number[:2].isupper():
            raise ValueError(f'No airline code in {number}')
        # 3) Last three are numbers
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f'Invalid route number {number}')
        # one _ means is a private variable
        self._number = number # create a 'private' variable

    # Methods are functions inside classes
    # Must have, self, as the first paramter
    def number(self):
        """Return the flight number

        Returns:
            string: Flight number
        """
        return self._number
    
    def airline(self):
        return self._number[:2]  # get airline code

def main():
    """
    Main Driver
    """
    f = Flight('SN403') # create an instance of the class flight
    # print(type(f))
    print(f.number())
    g = Flight('BW123')
    print(g.number())
    # g._number = 'TT456' # NOOOO
    # h = Flight('1#OIU')
    # h = Flight('ab123')
    # h = Flight('AB123555')
    h = Flight('AB155')
    print(f'Flight number {h.number()}')
    print(f'Airline code {h.airline()}')



if __name__ == '__main__':
    main()
    sys.exit(0)