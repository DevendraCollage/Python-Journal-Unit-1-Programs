# Python Journal Program - Unit-1
#  Definition : (C) PRINT ABOVE PYRAMID USING WHILE LOOP.
"""
1
3 5
7 9 11
13 15 17 19
"""

# Get the numbers user want to print
print("Enter the number : ", end="")
rows = int(input())
k = 1
i = 1

# Print the pyramid
while i <= rows:
    j = 1
    while j <= i:
        print(k, end=" ")
        k = k + 2
        j += 1
    print()
    i += 1

"""
Output :
1
3 5
7 9 11
13 15 17 19
21 23 25 27 29
"""
