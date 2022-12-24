# Python journal Program - Unit-1
# Definition : (E) WAP TO PRINT FOLLOWING PYRAMID USING FOR LOOP :
"""
1 2 3 6 12 24 48 …N .
"""

print("Enter Range : ", end="")
n = int(input())
j = 1
term = 0
print(1, 2, end=" ")
for i in range(1, n + 1):
    term = 3 * j
    print(term, end=" ")
    j = j + j

# Output :
"""
Enter Range : 10
1 2 3 6 12 24 48 96 192 384 768 1536
"""
