 # Programmer:   Connor Floyd
 # Course:       CSCI/ISAT B104
 # Assignment:   ICE 6.1
 
## Problem 1

print("\nThe purpose of this program is to determine eligibility for the SC Life Scholarship.")
print("------------------------------------------------------------------------------------")

print("\nAre you a South Carolina Resident? ")
resident_yn = input("Y/N: ").upper()

print("\nWhat is your High School GPA? ")
gpa = eval(input("GPA: "))

# sat
print("\nDid you take the SAT?")
sat_yn = input("Y/N: ").upper()

sat = 0
if sat_yn == "Y":
    print("\nWhat was your SAT score? ")
    sat = eval(input("SAT Score: "))

# act
print("\nDid you take the ACT?")
act_yn = input("Y/N: ").upper()

act = 0
if act_yn == "Y":
    print("\nWhat was your ACT score? ")
    act = eval(input("ACT Score: "))

# top 30%
print("\nDid you graduate in the top 30% of your High School class?")
top30 = input("Y/N: ").upper()

i = 0
if resident_yn == "Y":
    if gpa >= 3.0:
        i += 1
    if (sat >= 1100) or (act >= 24):
        i += 1
    if top30 == "Y":
        i += 1
    if i > 1:
        print("\nYou are eligible for the LIFE Scholarship!")
    else:
        print("\nYou are NOT eligible for the LIFE Scholarship.")
else:
    print("\nYou are NOT eligible for the LIFE Scholarship.")







