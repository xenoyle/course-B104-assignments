 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 11.1


## Step 1 - validation
## Step 2 - multiplication table
## Step 3 - row headers
## Step 4 - column headers
while True:
    try:
        size = input("\nSize: ")
        size = int(size)
        if size >= 2 and size <= 10:
            break
        else:
            print(f"{size} is NOT an integer between 2 and 10. Try again.\n")
    except:
        print(f"{size} is NOT an integer between 2 and 10. Try again.\n")


output = "\n"

for cols in range(1, size+1):
    output+="\t" + str(cols) 
output+="\n   "
for cols in range(1, size+1):
    output+="---" + " "
    
for rows in range(1, size+1):
    output+="\n"
    output+=f"{rows}|"
    for cols in range(1, size+1):
        output+="\t" + str(rows*cols)
        
print(output)
    
