'''
This code analyzes the Collatz conjecture as detailed below:

         n/2     -->   if  n ≡ 0 mod(2)
f(n) = {                                }
         3n+1    -->   if  n ≡ 1 mod(2)
'''

import numpy as np
import matplotlib.pyplot as plt
import math

print('\n\n==============================================================\n\n')

upperlimit = int(input('Select an upper limit:\n\n'))+1

# Function to determine is a number is even or odd
def Even_or_Odd_func(value):

	modVal = value % 2 		# Checks to see if a number is even or odd || Even --> 0 ; Odd --> != 0

	return(modVal)			# Returns the value from the modVal

	print(modVal)			# Prints the modVal

# Initializing empty matrix for value storage
MATRIX = np.zeros((upperlimit,2), dtype = int)	# Sets and empty matrix

print('\n\n==============================================================\n\n')

# Select a number to determine the number of steps for the conjecture
for x in range (1,upperlimit):

	# Initializing step value to determine the total number of steps needed until thr 4-2-1 loop
	step = 0				# Sets the first step value to be zero
	num = 4					# Dummy variable to allow the while loop to run

	# Loop to iterate until the 4-2-1 pattern occurs
	while num > 1: 				# Set to run to allow for the 4-2-1 loop

		if step == 0:

			newNum = int(Even_or_Odd_func(x))	# Determines if the value is even or odd for the initial number
			num = int(x)	# Saves the initial update as the recurring  variables

		else:

			newNum = int(Even_or_Odd_func(num))	# Determines if the value is even or odd

		if newNum == 0:

			num = int(num/2)	# Follows the conjecture rule for the even values

		else:

			num = int((3*num)+1)	# Follows the conjecture rule for the odd values

		if step == 0:

			MATRIX[x, 1] = step	# Saves the number of steps needed

		else:

			MATRIX[x,1] = np.log(step)
                		
		step = step + 1	# Increases the step value for each loop

	MATRIX[x, 0] = np.log(x)		# Saves the number at hand in the first column

# print('Number, No. of Steps')	        # Prints the column lables for the matrix
# print(MATRIX)				# Prints the matrix

# print('\n\n==============================================================\n\n')

# Plots the steps vs values
plt.plot(MATRIX[:,0],MATRIX[:,1],marker='.',linestyle='none',linewidth = 1)
plt.xlabel('Input Number')
plt.ylabel('Stopping Step')
plt.gcf()
plt.savefig('0thru100000_log.png')

print('Figure Saved\n\n')