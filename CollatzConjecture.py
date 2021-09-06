'''
This code analyzes the Collatz conjecture as detailed below:

         n/2     -->   if  n ≡ 0 mod(2)
f(n) = {                                }
         3n+1    -->   if  n ≡ 1 mod(2)
'''

import numpy as np
import matplotlib.pyplot as plt

print('\n\n==============================================================\n\n')

# Select a number to determine the number of steps for the conjecture
input_num = int(input('\nPlease Select a Number:    \n\n'))

print('\n\n==============================================================\n\n')

# Function to determine is a number is even or odd
def Even_or_Odd_func(value):

	modVal = value % 2 		# Checks to see if a number is even or odd || Even --> 0 ; Odd --> != 0

	return(modVal)			# Returns the value from the modVal

	print(modVal)			# Prints the modVal

# Initializing empty matrix for value storage
MATRIX = np.zeros((200,2), dtype = int)	# Sets and empty matrix

# Initializing step value to determine the total number of steps needed until thr 4-2-1 loop
step = 0				# Sets the first step value to be zero
num = 4					# Dummy variable to allow the while loop to run

# Loop to iterate until the 4-2-1 pattern occurs
while num > 1: 				# Set to run to allow for the 4-2-1 loop

	if step == 0:

		newNum = int(Even_or_Odd_func(input_num))	# Determines if the value is even or odd for the initial number
		num = int(input_num)	# Saves the initial update as the recurring  variables

	else:

		newNum = int(Even_or_Odd_func(num))	# Determines if the value is even or odd

	if newNum == 0:

		num = int(num/2)	# Follows the conjecture rule for the even values

	else:

		num = int((3*num)+1)	# Follows the conjecture rule for the odd values

	MATRIX[step, 0] = step		# Saves the step in the first column
	MATRIX[step+1, 1] = num		# Saves the pattern value in the second column of the matrix

	step = step + 1			# Increases the step value for each loop

MATRIX[0,1] = input_num
MATRIX[step,0] = int(step)
print('Step, Value')			# Prints the column lables for the matrix
print(MATRIX)				# Prints the matrix

print('\n\nThe number of steps needed is:',step-1)

print('\n\n==============================================================\n\n')

# Plots the steps vs values
plt.plot(MATRIX[0:153,0],MATRIX[0:153,1],marker='.',linestyle='-',linewidth = 1)
plt.title('Input Number is: 1000000')
plt.ylabel('Value')
plt.xlabel('Stopping Step')
plt.gcf()
plt.savefig('SingleNumber_1000000.png')


print('Figure Saved\n\n')