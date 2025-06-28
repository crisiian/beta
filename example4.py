import os

def calc(x, y):
    # Process
    add = x + y
    return add

####### Main ##########################################
# Inputs
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

ans = calc(num1, num2)

# Outputs form 1
print(f"The addition is: {ans}")

# Outputs form 2
print("The addition is: ", calc(num1, num2))