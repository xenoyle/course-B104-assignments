 # Programmer:   Connor Floyd
 # Course:       CSCI/ISAT B104
 # Assignment:   ICE 5.2

## Problem 1
# x = eval(input("Your number: "))
# if x > 7:
#     print(f"Yes, {x} is greater than 7.")
# elif x == 7:
#     print(f"Sorry, {x} is equal to 7.")
# else:
#     print(f"No, {x} is less than 7.")
    
## Problem 2
# resident = input("Are you an SC Resident? [Yes/No]: ")
# age = eval(input("What is your age? [years]: "))

# V1
# if resident == "Yes" and age >= 16:
#     print("You are eligible to earn an SC drivers license.")
# else:
#     print("You are NOT eligible to earn an SC drivers license.")
    
# V2
# if ((resident == "Yes") or (resident == "yes")) and (age >= 16):
#     print("You are eligible to earn an SC drivers license.")
# else:
#     print("You are NOT eligible to earn an SC drivers license.")
    
# V3
# if resident == "Yes" and age >= 16:
#     print("You are eligible to earn an SC drivers license.")
# elif resident == "yes" and age >= 16:
#     print("You are eligible to earn an SC drivers license.")
# else:
#     print("You are NOT eligible to earn an SC drivers license.")
    
## Problem 3
resident = input("Are you an SC Resident? [Yes/No]: ").upper()
age = eval(input("What is your age? [years]: "))

if resident == "YES" and age >= 16:
    print("You are eligible to earn an SC drivers license.")
else:
    print("You are NOT eligible to earn an SC drivers license.")