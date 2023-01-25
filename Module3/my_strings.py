#!/usr/bin/env python
'''
Practice string formatting
'''

name = 'Waldo'
school = 'WSU'
print('My name is', name, 'and my school is', school)

# Format the string
print('My name is {0} and my school is {1}'.format(name, school))

print('At {1}, my name is {0} and my school is {1}'.format(name, school))

# Format integers, floats, strings, etc
print('{0} {1} cost ${2}'.format(6, 'bananas', 1.56))

# Keyword arguments
print('{quantity} {item} cost ${price}'.format(
    item = 'bananas',
    quantity = 6,
    price = 1.56))

# Use f-strings
item = 'bananas'
quantity = 6,
price = 1.56
print(f'{quantity} {item} cost ${price}')

# Task: Calculate the area of a rectangle
length = 10.5
width = 5.21
area = length * width
print(f'The area of a rectangle with {length} length and {width} width is:{area}')
# Now use .format()
# Use {:f} for floating point notation
print(f'The area of a rectangle with {0:f} length and {1:f} width is:{2:f}'.format(
    length, width, area))
# use {:.2f} for floating point notation, with 2 digits of pre.
print('The area of a rectangle with {0:.3f} length and {1:.3f} width is:{2:.3f}'.format(
    length, width, area))
# Use {:6.2f} for floating point notation, with 6 digits width AND 2 digits of pre.
print('The area of a rectangle width[{0:08.2f}] length and [{1:08.2f}] width is: [{2:08.2f}]'.format(length, width, area))

# Use some string methods
city = 'ogden'
print(f'{city.capitalize()}') # only capitalize the first letter
print(f'{city.upper()}') # All caps

# Strings as collections
school = 'Weber State University'
print(f'The length of{school} is {len(school)} characters long')