 # Programmer:   Connor Floyd
 # Course:       CSCI/ISAT B104
 # Assignment:   ICE 4.2


    ## Problem 1
print('\n\n **** Problem 1 ****')

fruits = ["apple","banana","coconut","dragonfruit"]

for f in fruits:
    print(f)

    ## Problem 2
print('\n\n **** Problem 2 ****')

studentAges = [18,25,19,43,21,18,19]
studentAges.sort(reverse=True)
for age in studentAges:
    print(age)

    ## Problem 3
print('\n\n **** Problem 3 ****')

fruits = ["apple","banana","coconut","dragonfruit"]
fruits[2] = "cherry"

for f in fruits:
    print(f)
    
    ## Problem 4
print('\n\n **** Problem 4 ****')

print(fruits[2])

    ## Problem 5
print('\n\n **** Problem 5 ****')
fruits.append("elderberry")
print(fruits[4])

    ## Problem 6
print('\n\n **** Problem 6 ****')
print(f"The last fruit in out list is: {fruits[-1]}")
print(f"The 2nd to last fruit in out list is: {fruits[-2]}")

    ## Problem 7
print('\n\n **** Problem 7 ****')

Numbers = range(6)
for i in Numbers:
    print(i)
    
    ## Problem 8
print('\n\n **** Problem 8 ****')

evenNumbers = range(0, 10, 2)
for i in evenNumbers:
    print(i)
    

