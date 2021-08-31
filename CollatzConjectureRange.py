step = 0                                # Sets the first step value to be zero
num = 4                                 # Dummy variable to allow the while loop to run

# Loop to iterate until the 4-2-1 pattern occurs
while num > 1:                          # Set to run to allow for the 4-2-1 loop

        if step == 0:

                newNum = int(Even_or_Odd_func(input_num))       # Determines if the value is even or odd for the initial number
                num = int(input_num)    # Saves the initial update as the recurring  variables

        else:

                newNum = int(Even_or_Odd_func(num))     # Determines if the value is even or odd

        if newNum == 0:

                num = int(num/2)        # Follows the conjecture rule for the even values

        else:

                num = int((3*num)+1)    # Follows the conjecture rule for the odd values

        MATRIX[step, 0] = step          # Saves the step in the first column
        MATRIX[step, 1] = num           # Saves the pattern value in the second column of the matrix

        step = step + 1                 # Increases the step value for each loop

print('Step, Value')                    # Prints the column lables for the matrix
print(MATRIX)                           # Prints the matrix

print('\n\nThe number of steps needed is:',step,)

print('\n\n==============================================================\n\n')

# Plots the steps vs values
# plt.plot(MATRIX[:,0],MATRIX[:,1])
# fig = plt.figure()
# fig.savefig('test.png')
# plt.show
