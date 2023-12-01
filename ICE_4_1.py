 # Programmer:   Connor Floyd
 # Course:       CSCI/ISAT B104
 # Assignment:   ICE 4.1

     
## Problem 1
print("\t **** Problem 1 ****")

temp_f = eval(input("What is the temperature in degrees (F): "))
temp_c = (temp_f - 32) * (5 / 9) 
print(f"The current temperature on the Bluffton campus is {round(temp_f, 2)} degrees F ({round(temp_c, 2)} degrees C) \n")

## Problem 2
print("\t **** Problem 2 ****")

km_per_miles = 1.60934
miles_between_campuses = 41.0
km_between_campuses = km_per_miles * miles_between_campuses
print(f"The distance between the Beaufort and Hilton Head USCB campuses is {round(miles_between_campuses, 2)} miles ({round(km_between_campuses, 2)} kms)")