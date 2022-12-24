# Python Journal Program - Unit-1
# Definition : WAP TO GET 2 NUMBER FROM THE USER AND PRINT EVEN NUMBER USING WHILE LOOP.

# Get the two numbers from the user
print("Enter Number One : ", end="")
num1 = int(input())
print("Enter Number Two : ", end="")
num2 = int(input())
# Print the even number if the number is even
print("Your Even Number Is : ")
while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
    num1 += 1

# Output :
"""
Enter Number One : 2
Enter Number Two : 10
Your Even Number Is :
2
4
6
8
10
"""
