# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# first we need to define the function and ask for to arguments
def compare(a,b):
#case 1 when the first number is greater than the second number  
  if a > b :
    return 1
# case 0 when the twon numbers are equals
  elif a == b:
    return 0
# case -1 when the the second number is greater than the first one
  else :
    return -1
# now testing the 3 cases by static values
print (compare(5,2))
print (compare(2,5))
print (compare(3,3))

# prompting and storing the first number
user_input_A = input("Please enter the first number to compare\n")
#prompting and storing the second number
user_input_B = input("Please enter the first number to compare\n")
# compare and print the return value
print(compare(user_input_A,user_input_B))


   
     
   

    
