# Python Journal Program - Unit-1
# Definition :(D) PRINT ABOVE PYRAMID USING WHILE LOOP.
"""
1
1 2
3 5 8
13 21 34
…N
"""

# Get the number from the user want to print
print("Enter a number : ", end="")
rows = int(input())
a = 0
b = 1
c = a + b
i = 1

# Print the pyramid
while i <= rows:
    j = 1
    while j <= i:
        print(c, end=" ")
        c = a + b
        a = b
        b = c
        j += 1
    print()
    i += 1

"""
Output :
Enter a number : 5
1
1 2
3 5 8
13 21 34 55
89 144 233 377 610
"""
