 # Programmer:   Connor Floyd
 # Course:       CSCI/ISAT B104
 # Assignment:   ICE 4.3
 
## Problem 1
print('\n\n **** Problem 1 ****')
# Create a script which outputs to the console
# window all the even numbers from -12 to 12

evenNumbersList = range(-12,13,2)
for i in evenNumbersList:
    print(i)
    
    
## Problem 2
print('\n\n **** Problem 2 ****')
# Create a script which prompts the user for two numbers
# It then outputs to the console all the numbers between them
# Assume that the first number entered by the user is the smaller number
# Do not include two numbers used by user

A = eval(input("Enter the smaller number for range: "))
B = eval(input("Enter the larger number for range: "))
final = range(A+1,B)
for i in final:
    print(i)
    

## Problem 3
print('\n\n **** Problem 3 ****')
# Create a script which prompts the user for two numbers
# It then outputs to the console all the numbers between them
# Counting down from the larger to the smaller
# Do not include two numbers used by user
# Assume first number is larger number

C = eval(input("Enter the larger number for range: "))
D = eval(input("Enter the smaller number for range: "))
finale = range(C-1,D,-1)
for i in finale:
    print(i)