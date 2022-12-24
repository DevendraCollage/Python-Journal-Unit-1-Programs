# Python journal Program - Unit-1
# Definition : (B) PRINT ABOVE PYRAMID USING WHILE LOOP.
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# Get the number user want to print
print("Enter a number :", end=" ")
rows = int(input())
i = 0

# Display the pyramid of the (Number)
while i <= rows:
    j = 0
    while j <= i:
        print(j + 1, end=" ")
        j += 1
    print()
    i += 1

"""
Output :
Enter a number : 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
