# Python Journal Program - Unit-1
# Definition : WAP TO PERFORM ARITHMETIC OPERATION USING FUNCTION.

# Get the input from the user
print("Enter Number One : ", end="")
num1 = int(input())
print("Enter Number Second : ", end="")
num2 = int(input())


# Create A Function
def arith():
    # Addition
    print("Your", num1, "And", num2, "Addition Is :", num1 + num2)
    # Multiplication
    print("Your", num1, "And", num2, "Multiplication Is :", num1 * num2)
    # Subtraction
    print("Your", num1, "And", num2, "Subtraction Is :", num1 - num2)
    # Division
    print("Your", num1, "And", num2, "Division Is :", num1 / num2)


# Call the Function
arith()

# Output :
"""
Enter Number One : 10
Enter Number Second : 5
Your 10 And 5 Addition Is : 15 
Your 10 And 5 Multiplication Is : 50 
Your 10 And 5 Subtraction Is : 5 
Your 10 And 5 Division Is : 2.0 
"""
