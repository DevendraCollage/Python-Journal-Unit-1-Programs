# Python Journal Program - Unit-1
# Definition : WAP TO PRINT TABLE OF 5.

# Get the User input want to print
print("Enter The Table Number : ", end="")
table = int(input())
# Print The Table
for i in range(1, 11):
    print(table, 'x', i, '=', table * i)

# Output :
"""
Enter The Table Number : 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""
