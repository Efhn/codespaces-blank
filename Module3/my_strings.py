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
print('The area of a rectangle with {0} length and {1} width is:{2}'.format(length, width, area))
