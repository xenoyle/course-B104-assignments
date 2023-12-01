 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 9.1
 
 
## Problem 1
# x = 1
# while x < 10:
#     x+=1
#     print(x)
    
## Problem 2
color = "GREEN"
print("What color is the stop light?")
color = input("Stop light color: ").upper()

while color != "GREEN":
    if color == "RED":
        print("\nStop")
    elif color == "YELLOW":
        print("\nSlow Down")
    else:
        print("\nThrow away your drivers license.")
    
    print("\n\nWhat color is the stop light NOW?")
    color = input("Stop light color: ").upper()
    
print("\n Go GO GO GO!!")
    