# Python Journal Program - Unit-1
# Definition : WAP TO CHECK ENTERED NUMBER IS ODD OR EVEN

# Get the number from the user
print("Enter the Number : ", end="")
number = int(input())
# Check the number is odd or even
if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# Output :
"""
Enter the Number : 10
Number is Even

Enter the Number : 3
Number is Odd
"""