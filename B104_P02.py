 # Programmer:  Connor Floyd
 # Course:      CSCI/ISAT B104
 # Assignment:  Practical 02 (P02)
 # File Name:   B104_P02.py
 
print("Practice Practical #2: Evens and Odds")
print("-------------------------------------")
print("\nWhat is your smaller number?")
small_number = eval(input("Smaller number: "))
print("\nWhat is your larger number?")
large_number = eval(input("Larger number: "))
print("\n")

for number in range(small_number,large_number+1):
    if number % 2 == 0:
        print(f"{number}.\tEven")
    else:
        print(f"{number}.\tOdd")