'''
This code analyzes the Collatz conjecture as detailed below:

         n/2     -->   if  n ≡ 0 mod(2)
f(n) = {                                }
         3n+1    -->   if  n ≡ 1 mod(2)
'''

import math as m

number = int(input('Please Select a Number:    \n\n'))

def Even_or_Odd_func(value):

	newVal = value % 2

	return(newVal)

while iter > 1:
