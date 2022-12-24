# Python Journal Program - Unit-1
# Definition: (A) PRINT ABOVE PYRAMID USING WHILE LOOP.
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
i = 0

# Display the pyramid of (*)
while i <= rows:
    j = 0
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

"""
Output :
Enter number of rows : 5
*
* *
* * *
* * * *
* * * * *
"""
