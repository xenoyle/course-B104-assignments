 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 8.1
 


print("\nPractical 02: Evens and Odds")
print("-----------------------------")

print("What is your smaller number?")
small_num = int(input("Smaller Number: ")) ## ASSUMING USER GIVES INTEGER (ValueError if not integer)

print("\nWhat is your larger number?")
large_num = int(input("Larger Number: "))
print(" ")

## V1
# for i in range(small_num, large_num + 1, 1):
#     if (i % 2 == 0):
#         print(f"{i}.\t Even")
#     else:
#         print(f"{i}.\t Odd")

## V2
# for i in range(small_num, large_num + 1, 1):
#     if (i % 2 == 0):
#         print(f"{i}.\t Even")
#     elif (i % 2 != 0):
#         print(f"{i}.\t Odd")
    
## V3
# for i in range(small_num, large_num + 1, 1):
#     if (i % 2 == 0):
#         print(f"{i}.\t Even")
#     elif (i % 2 == 1):
#         print(f"{i}.\t Odd")

## V4
for i in range(small_num, large_num + 1, 1):
    if (i % 2 == 0):
        print(f"{i}.\t Even")
    if (i % 2 == 1):
        print(f"{i}.\t Odd")
    
