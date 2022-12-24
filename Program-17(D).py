# Python journal Program - Unit-1
# Definition :(D) WAP TO PRINT FOLLOWING PYRAMID USING FOR LOOP :
"""
1
1 2
3 5 8
13 21 34
…N
"""

start = 0
second = start + 1
end = 6
for j in range(1, 5):
    for k in range(1, j + 1):
        next = start + second
        start = second
        second = next
        print(start, end=" ")
    print()

# Output :
"""
1
1 2
3 5 8
13 21 34 55
"""