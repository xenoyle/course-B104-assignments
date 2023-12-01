 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 11.2


# function definition - version 1
# def FizzBuzz(x):
#     return_value = ""
#     if x%3==0 and x%5==0:
#         return_value = "Fizz Buzz"
#     elif x%5==0:
#         return_value = "Buzz"
#     elif x%3==0:
#         return_value = "Fizz"
#     else:
#         return_value = ""
#     return return_value


# function definition - version 2
def FizzBuzz(x):
    if x%3==0 and x%5==0:
        return "Fizz Buzz"
    elif x%5==0:
        return "Buzz"
    elif x%3==0:
        return "Fizz"
    else:
        return ""


# driver - version 1
# for i in range(1,20+1):
#     return_value = FizzBuzz(i) # this calls the function!!
#     print(f"{i}.\t{return_value}")


# driver - version 2
for i in range(1,20+1):
    print(f"{i}.\t{FizzBuzz(i)}")