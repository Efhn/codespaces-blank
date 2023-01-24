'''
A temperature converter from Celsius to Farenheit
'''

# Formula: F = (C * 9/5) + 32
TEMP_CONSTANT_P1 = 9/5
TEMP_CONSTANT_P2 = 32

celsius = float(input('Enter the temperature in Celsius: '))
feranheit = celsius * TEMP_CONSTANT_P1 + TEMP_CONSTANT_P2
print('The equivalent temperature of', 'Celsius in Farenheit is', feranheit)
