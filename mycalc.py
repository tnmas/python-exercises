# code for a simple python calculator

#prompt the user to input the first number.
        
num1=int(input("Enter first number: "))
while(num1==0):
    print("Error")
    num1=int(input("Enter first number: "))

#accepts the operator.
        
print("1-add,  2-subtract,  3-multiply,  4-divide")

operator=int(input("Enter operator: "))
while(operator<1 or operator>4):
    print("Error")
    operator=int(input("Enter operator: "))

#prompt the user to input the second number
num2=int(input("Enter a second number: "))
while(num2==0):
    print("Error")
    num2=int(input("Enter a second number: "))
        

if(operator==1):
    result=num1+num2
elif(operator==2):
    result=num1-num2
elif(operator==3):
    result=num1*num2
else:
    result=num1/num2
print(result)
    
