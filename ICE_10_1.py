 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 10.1




# review problem #1:
# using a for loop, loop from 5 to 15 (inclusive).
# at each step, print out the number

# for i in range(5,15+1):
#     print(i)


# review problem #2:
# using a while loop, loop from 5 to 15 (inclusive).
# at each step, print out the number

# i = 5
# while i <= 15:
#     print(i)
#     i+=1
    

# review problem #3:
# using a while loop, loop from smaller to larger number (inclusive).
# at each step, print out the number
# you can assume that the 1st number is smaller and 2nd number
# is larger.
# you can also assume the numbers are integers

# small = int(input("\nSmaller number: "))
# large = int(input("Larger number: "))
# print("\n")
# while small <= large:
#     print(small)
#     small+=1


# review problem #4:
# using a while loop, loop from smaller to larger number (inclusive).
# at each step, print out the number
# not known which number is larger or smaller
# you can assume the numbers are integers

num1 = int(input("\nFirst Number: "))
num2 = int(input("Second Number: "))
print("\n")
if num1 < num2:
    while num1 <= num2:
        if num1%2==0:
            print(num1)
        num1+=1
elif num1 > num2:
    while num1 >= num2:
        if num2%2==0:
            print(num2)
        num2+=1
elif num1%2==0:
    print(num1)

