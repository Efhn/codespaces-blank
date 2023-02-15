#!/usr/bin/env python
"""
Compute as estimate of PI by simulating dart throws onto a square.
"""

from random import random

TRIES = 100

hits = 0

for index in range(TRIES):
    # Generate two randoms numbers between -1 and 1
    r = random()
    x = -1 + 2 * r 
    r = random()
    y = -1 + 2 * r
    # Check if point lies in the unit circle
    if x*x + y*y <= 1:
        hits = hits + 1

# The ratio hits/tries is approximately the same as the ratio 
# (circle area)/(square area)
estimated_pi = 4.0*hits/TRIES
print(f'Estimated calculation for PI is: {estimated_pi}')