 # Programmer:   Connor Floyd
 # Course:       CSCI/ISAT B104
 # Assignment:   ICE 3.2
 
import math

 # Problem
 # Prompt the user for the radius of a circle.
 # Calculate the area of the circle
 # Then provide output to the user informing them of
 # the results. The output should be of the form:
 #      A circle with radius ___ has area ___

## Version 1
# r = eval(input("Radius of circle: "))
# a = 3.14 * (r * r)
# print("A circle with radius " + str(r) + " has the area " + str(a) + ".")

## Version 2
r = eval(input("Radius of circle: "))
a = math.pi * math.pow(r,2)
print(f"A circle of radius {r} has area {round(a, 2)}.")
 