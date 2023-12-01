 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 7.2

## Problem 1
## Solicit a whole number between 0 and 20 from the user.
## Print out each number between 10 and the user's number.
## If user number is 10, print 10.

userNumber = eval(input("Please enter a number (0-20): "))

if userNumber == 10:
    print(10)
elif userNumber > 10:
    for number in range(10+1,userNumber,1):
        print(number)
else:
    for number in range(userNumber+1,10,1):
        print(number)
        
        
## Problem 2
## Solicit a whole number between 0 and 20 from the user.
## Determine if the number is even or odd.
## If even, print even. If odd, print odd.

userNumber2 = eval(input("Please enter a number (0-20):"))

if (userNumber2 % 2) == 1:
    print(f"The number {userNumber2} is ODD.")
else:
    print(f"The number {userNumber2} is EVEN.")
    

## Problem 3
## Solicit a whole number between 0 and 20 from the user.
## Print out each ODD number between 10 and the user's number.
## If user number is 10, print 10.

userNumber3 = eval(input("Please enter a number (0-20): "))

if userNumber3 == 10:
    print("You are a very intelligent specimen. :)")
elif userNumber3 > 10:
    for number in range(10,userNumber3,1):
        if number % 2 == 1:
            print(number)
else:
    for number in range(userNumber3,10,1):
        if number % 2 == 1:
            print(number)