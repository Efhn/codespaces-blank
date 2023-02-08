#!/usr/bin/env python
"""
Display the description of some radiation given its wavelength
"""

import sys

RADIO = 0 
MICROWAVE = 1
INFRARED = 2
VISIBLE = 3
ULTRAVIOLET = 4
X_RAYS = 5
GAMMA = 6
RADIATION_TYPES = ['Radio Waves', 'Microwaves', 'Infrared',
                   'Visible light', 'Ultraviolet', 'X-Rays', 'Gamma Rays' ]
# TODO: Capture the frequency
frequency = float(input('Enter the frequency. ex: 3e12 '))

# TODO: Display the description of the radiation
# Less than or equal 3e9: Radio waves
if frequency <= 3e9:
    rad_level = RADIO
# More than 3e9 and less than or equal 3e11: Microwaves
elif frequency > 3e9 and frequency <= 3e11:
    rad_level = MICROWAVE
# More than equal 3e11 and less than or equal 4e14: Infrared
elif frequency > 3e11 and frequency <= 4e14:
    rad_level = INFRARED
# More than equal 4e14 and less than or equal 7.5e14: Visible light
elif frequency > 4e14 and frequency <= 7.5e14:
    rad_level = VISIBLE 
# More than equal 7.5e14 and less than or equal 3e16: Ultraviolet
elif frequency > 7.5e14 and frequency <= 3e16:
    rad_level = ULTRAVIOLET
# More than equal 3e16 and less than or equal 3e19: X-Rays
elif frequency > 3e16 and frequency <= 3e19:
    rad_level = X_RAYS
# More 3e19: Gamma rays
else:
    rad_level = GAMMA



# Less than or equal 3e9: Radio waves
# More than or equal 3e9 and less than or equal 3e11: Microwaves
# More than equal 3e11 and less than or equal 4e14: Infrared
# More than equal 4e14 and less than or equal 7.5e14: Visible light
# More than equal 7.5e14 and less than or equal 3e16: Ultraviolet
# More than equal 3e16 and less than or equal 3e19: X-Rays
# More 3e19: Gamma rays
