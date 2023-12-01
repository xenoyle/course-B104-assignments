 # Programmer:  Connor Floyd
 # Course:      CSCI/ISAT B104
 # Assignment:  Practical 01 (P01)
 # File Name:   ICE 7.1
 
import csv
 
colors = ["red", "yellow", "green", "blue"]
cars = ["BMW", "Subaru", "Mini", "Lexus", "Honda"]

with open("C:/Users/cwfloyd/Desktop/B104/cars.csv", "w", encoding="UTF-8", newline="") as f:

    writer = csv.writer(f)

    for color in colors:
        for car in cars:
            ##print(f"{color} {car}")
            row = [color,car]
            writer.writerow(row)