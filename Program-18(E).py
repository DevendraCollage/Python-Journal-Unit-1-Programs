# Python Journal Program - Unit-1
# Definition : PRINT ABOVE PYRAMID USING WHILE LOOP.
"""
1 2 3 6 12 24 48 …N
"""

# Get the number from the user want to print
print("Enter a number : ", end="")
rows = int(input())
r = 5
a = 1
b = 2
print(a, b, r, end=" ")
i = 1

# Print the number
while i < rows:
    r *= 2
    print(r, end=" ")
    i += 1

"""
Output : 
Enter a number : 10
1 2 3 6 12 24 48 96 192 384 768 1536
"""
