 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         Programming Exercises 10.1

# store variables in a list of lists, then print one list at a time after calculating what will be in each list

print("\nThe purpose of this program is to create a multiplication table.")
print("The program will ask you for the size of the table, which must be from 2 to 10 (inclusive).")
print("--------------------------------------------------------------------------------------------\n")
z = 0
while z == 0:
    try:
        size = int(input("Size: "))
        if size < 2 or size > 10:
            print("That was not a number from 2-10, try again please.\n")
            continue
        z+=1
    except:
        print("That was not an integer, try again please.\n")

table = []

## COLUMN HEADER CREATION
temp = ["\n"]
for i in range(1,size+1): 
    temp.append(str(i))
for i in temp:  
    print(i, end="\t") # creates the column headers
    
temp = ["\n  "]
for i in range(1,size+1): 
    temp.append("---")
for i in temp:  
    print(i, end=" ") # creates the underlines
## TABLE DATA CREATION
i = 1
while i <= size:   
    temp = [f"\n{i}|"]
    for j in range(1,size+1):
        temp.append(f"{i*j}")
    table.append(temp)
    i+=1
## PRINT TABLE
for i in table:  
    temp = i
    for i in temp:
        print(i, end="\t") # creates the multiplication table
    



