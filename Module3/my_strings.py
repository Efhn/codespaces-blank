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
