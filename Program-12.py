# Python Journal Program - Unit-1
# Definition : WAP TO GET 2 NUMBER FROM THE USER AND PRINT PALINDROME NUMBER.
print("Enter Minimum Number : ", end="")
min1 = int(input())
print("Enter Maximum Number : ", end="")
max1 = int(input())
print("Palindrome Number Are : ", end="")
for i in range(min1, max1 + 1):
    temp = i
    rev = 0
    while temp > 0:
        ren = temp % 10
        rev = (rev * 10)
        temp = temp // 10
    if i == rev:
        print(i, end=" ")


"""
Output :
Enter Minimum Number : 10
Enter Maximum Number : 100
Palindrome Number Are : 
11  22  33  44  55  66  77  88  99
"""