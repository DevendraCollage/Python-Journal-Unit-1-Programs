# Python Journal Program - Unit-1
# Definition :(C) WAP TO PRINT FOLLOWING PYRAMID USING FOR LOOP :
"""
1
3 5
7 9 11
13 15 17 19
"""

# Get the number user want to print
print("Enter a Number : ", end="")
rows = int(input())
k = 1
# Display the pyramid of the (odd numbers)
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        k += 2
    print()


# Output :
"""
1
3 5
7 9 11
13 15 17 19
"""