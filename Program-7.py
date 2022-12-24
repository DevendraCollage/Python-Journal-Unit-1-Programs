# Python Journal Programs - Unit-1
# Definition : WAP TO GET NUMBER FROM USER AND CHECK > 18 OR NOT IF YES THEN PRINT ELIGIBLE OTHERWISE NOT ELIGIBLE.

# Get the age from the user
print("Enter Your Age : ", end="")
age = int(input())
# Check the age if age > 18 the print or not eligible
if age > 18:
    print("You are eligible")
else:
    print("You are not eligible")


# Output :
"""
Enter Your Age : 25
You are eligible

Enter Your Age : 15
You are not eligible
"""