# Python Journal Programs - Unit-1
# Definition : WAP TO DETERMINE IF CONDITION.

print("Enter A : ", end="")
a = input()
print("Enter B : ", end="")
b = input()
print("Enter C : ", end="")
c = input()

# A is larger than b and c then print a
if a > b and a > c:
    print("A is largest")
# B is larger than a and c then print b
if b > a and b > c:
    print("B is largest")
# C is larger than a and b then print c
if c > a and c > b:
    print("C is largest")


# Output :
"""
Enter A : 20
Enter B : 50
Enter C : 10
B is largest
"""