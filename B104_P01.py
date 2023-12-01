 # Programmer:  Connor Floyd
 # Course:      CSCI/ISAT B104
 # Assignment:  Practical 01 (P01)
 # File Name:   B104_P01.py
 
## Task 1
print("Purpose: This program calculates the area of a donut.")
print("-----------------------------------------------------")
don_diameter = eval(input("\nDiameter (donut): "))
donhole_diameter = eval(input("\nDiameter (donut hole): "))
don_radius = don_diameter / 2
donhole_radius = donhole_diameter / 2
pi = 3.14
don_area = pi * (don_radius**2)
donhole_area = pi * (donhole_radius**2)
total_area = don_area - donhole_area
print(f"\nA donut of width {don_diameter} with a hole of width {donhole_diameter} has area {round(total_area, 2)}")
