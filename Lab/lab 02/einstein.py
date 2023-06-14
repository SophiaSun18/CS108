"""CS 108 - Lab 2.1

Imitates the Einstein's Number Puzzle

@author: Samuel Fincher (smf39)
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Gets a 3 digit number input from the user
number = int(input('Number: '))

# Finds the digits of number in 100's, 10's and 1's
digit1 = number // 100
digit2 = (number - (digit1 * 100)) // 10
digit3 = (number % 10)

# Reverses number to get rev_number
rev_number = int(str(digit3) + str(digit2) + str(digit1))

# Finds the positive difference between number and rev_number
difference = abs(number - rev_number)

# Finds the digits of difference in 100's, 10's and 1's
# Reverses difference to get rev_diff
diff_1 = difference // 100
diff_2 = (difference - (diff_1 * 100)) // 10
diff_3 = (difference % 10)
rev_diff = int(str(diff_3) + str(diff_2) + str(diff_1))

# Prints the sum of difference and rev_diff
print(difference + rev_diff)