 # Programmer:   Connor Floyd
 # Course:       CSCI/ISAT B104
 # Assignment:   ICE 5.1
 

## Problem 1
print('\n\n **** Problem 1 ****')
x_pennies = 2**29
x_dollars = x_pennies/100

if x_dollars > 1000000:
    print(f"The amount earned via pennies is: {x_dollars: .2f}")
else:
    print("Take the million")
    

## Problem 2
print('\n\n **** Problem 2 ****')
chessArea = 8*8
temp = 1
tempValue = 0
grains_total = 0
## CONNOR FLOYD VERSION OF ACCUMULATION
# for i in range(0,64,1):
#     tempValue = tempValue+(2**i) 


##PROFESSOR ERDEI VERSION OF ACCUMULATION
for s in range(1, 64+1, 1):
    power = s-1
    grains_on_that_square = 2 ** power
    grains_total = grains_total + grains_on_that_square

## BOTH WORK
print(grains_total)

grains_grams = grains_total * 0.065
grains_tons = grains_grams / 1000000

print(grains_tons)



    