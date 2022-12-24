# Python Journal Program - Unit-1
# Definition : (F) WAP TO PRINT FOLLOWING PYRAMID USING FOR LOOP :
"""
1 4 9 16 25 36 … N
"""

print("Enter Range : ", end="")
n = int(input())
for i in range(1, n + 1):
    print(i * i)


# Output :
"""
Enter Range : 10
1
4
9
16
25
36
49
64
81
100
"""