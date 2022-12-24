# Python Journal Programs - Unit-1
# Definition : WAP TO GET 2 NUMBER FROM THE USER AND PRINT FIBONACCI SERIES.

print("Enter Start Number : ", end="")
start = int(input())
print("Enter End Number : ", end='')
end = int(input())
second = start + 1
print("Fibonacci Series : ")
for i in range(start, end):
    print(start)
    next = start + second
    start = second
    second = next

# Output :
"""
Fibonacci Series : 
0
1
1
2
3
5
8
13
"""
