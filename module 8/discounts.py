#!/usr/bin/env python
"""
Module documentation
"""
import sys


def apply_discount(amt, *percentage, **kwargs):
    total = sum(amt)
    discount = total*percentage[0]/100
    return total - discount


def percentage_discount(percent, *args, **kwargs):
    return apply_discount(percent, *args)


def checkout(cart, *discount):
    total = sum(cart)
    discount_type = discounts[0] # callable function
    discount_amount = discounts[1] # amount
    total = discount_type(total, discount_amount)
    return total

def main():
    """
    Main Driver
    """
    cart = [10, 20, 30]
    discount = checkout(cart, percentage_discount, 10)
    print(f'Your total is{sum(cart)}')
    print(f'Your discount is {discount}')


    if __name__ == '__main__':
        main()
        sys.exit(0)