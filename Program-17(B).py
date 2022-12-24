# Python Journal Program - Unit-1
# Definition :(B) WAP TO PRINT FOLLOWING PYRAMID USING FOR LOOP :
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# Get the number user want to print
print("Enter a Number : ", end="")
rows = int(input())

# Display the pyramid of (number)
for i in range(rows):
    for j in range(i+1):
        print(j+1, end="")
    print("\r")


# Output :
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""