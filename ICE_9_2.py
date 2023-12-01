 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 9.2
 
 
 
## Version 1
# while True:
#     try:
#         x = input("Number: ")
#         x = int(x)
#         print(f"{x} is an integer.")
#         break
#     except:
#         print(f"{x} is NOT an integer.")
 
 
## Version 2
# validInput = False
# while validInput == False:
#     try:
#         x = input("Number: ")
#         x = int(x)
#         print(f"{x} is an integer.")
#         validInput = True
#     except:
#         print(f"{x} is NOT an integer.")
 


## Version 3
# Problem: Solicit a whole number between 2 and 10, then 
# print out the cube of that number
print("\nPlease provide a whole number between 2 and 10 (inclusive)")
while True:
    try:
        x = input("\nNumber: ")
        x = int(x)
        if (x >= 2) and (x <= 10):
            break
        else:
            print(f"{x} is not a good input.")
    except:
        print(f"{x} is not a good input.")
print(f"The cube of x is {x**3}.")

