 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         Practical 3

## Task 1: Print informative information first
## Task 2: Prompt user for integer between 10 and 35 inclusive with input validation
## Task 3: Iterate from 1 to the prompted integer and print it out with a period after.
## Task 4: If the number is multiple of 3, print Sand after, if 5, Shark! after, if both, Sandshark!

print("\nPractical #3: Sandshark!")
print("------------------------")
z = 0
while z == 0:
    try:
        x = input("\nPlease input an integer between 10 and 35 (inclusive):")
        x = int(x)
        if x >= 10 and x <= 35:
            z+=1
        else:
            print(f"{x} is not an integer from 10 to 35, please try again.")
    except:
        print(f"{x} is not an integer from 10 to 35, please try again.")
        
for i in range(1,x+1):
    if i%3==0 and i%5==0:
        print(f"{i}. Sandshark!")
    elif i%5==0:
        print(f"{i}. Shark!")
    elif i%3==0:
        print(f"{i}. Sand")
    else:
        print(f"{i}.")