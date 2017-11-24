""" 
Week 6 Programming assignment. Comparing function
"""

def compare (a, b): #Here we are defining our function
    if a == b:      
        answer = 0
    elif a > b:
        answer = 1
    elif a < b:
        answer = -1
    return answer

    # Static calls 
print ("We are comparing 5 and 2, using function compare. Function returns: " , compare(5,2))
print ("We are comparing 2 and 5, using function compare. Function returns: " , compare(2,5))
print ("We are comparing 3 and 3, using function compare. Function returns: " , compare(3,3))

    # user input part
user_input_a = input("Please enter number one: ") 
user_input_b = input("Please enter number two: ")
print("After comparing ", user_input_a, " and ", user_input_b, ", function returns: ", compare(user_input_a, user_input_b))