# Python Journal Program - Unit-1
# Definition : WAP TO PRINT NUMBER IS POSITIVE,NEGATIVE OR ZERO

# Get the number from the user
print("Enter The Number : ", end="")
number = int(input())
# Check the number is positive,negative or zero
if number > 0:
    print("Number is Positive")
elif number == 0:
    print("Number is Zero")
else:
    print("Number is Negative")


# Output :
"""
Enter The Number : 10
Number is Positive

Enter The Number : 0
Number is Zero

Enter The Number : -10
Number is Negative
"""