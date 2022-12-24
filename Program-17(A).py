# Python Journal Program - Unit-1
# Definition :(A) WAP TO PRINT FOLLOWING PYRAMID USING FOR LOOP :
"""
*
* *
* * *
* * * *
* * * * *
"""

# Get the number user want to print
print("Enter number of rows : ", end="")
rows = int(input())

# Display the pyramid of (*)
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print("\r")


# Output :
"""
*
* *
* * *
* * * *
* * * * *
"""
