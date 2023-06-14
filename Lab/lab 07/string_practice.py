"""CS 108 - Lab 7.0

This module reads a name from the user and outputs the shortened form of the name in the British English style.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Gets a name from the user and splits the name into a list of names.
name = input('Full Name: ')
name_s = name.split(' ')

# Decides the form of the name and outputs the corresponding shortened form.

# If the name has the form of firstname - middlename - lastname, the output will be lastname - initial of the firstname - initial of the middlename.
if len(name_s) == 3:
    firIni = name_s[0]
    midIni = name_s[1]
    lastName = name_s[2]
    print('{}, {}.{}.'.format(lastName, firIni[0], midIni[0]))
    
# If the name has the form of firstname - lastname, the output will be lastname - initial of the firstname.
elif len(name_s) == 2:
    firIni = name_s[0]
    lastName = name_s[1]
    print('{}, {}.'.format(lastName, firIni[0]))

# If the name is in other forms, the output will be an error message.
else:
    print("'{}' is a non-standard name.".format(name))