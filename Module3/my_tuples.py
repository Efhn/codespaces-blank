#!/usr?bin?env python
'''
Learn about Python Tuples
'''

t = ('Ogden', 123, 9.67)
# Print the tuple
print(type(t), t)
# Print one element
print(f'First element {t[1]}')
# Get total elements
print(f'Total elements {len(t)}')
# Print last element
print(f'Last element {t[len(t) - 1]}')
# Negative indexing
print(f'Last element {t[-1]}')

# Nested Tuples
coordinates = ((220, 123), (1164, 345), (3456, 21))
print(f'Coordinates = {coordinates}')
print(f'Coordinates first element = {coordinates[0]}')
print(f'Coordinates second element of third collection = {coordinates[2][1]}')
print(f'Coordinates 3-levels down collection = {coordinates([1][1][1])}')

# Single elements tuples
solo = (3,) # add a comma
print(f'Sole type {type(solo)}, value {solo}')


