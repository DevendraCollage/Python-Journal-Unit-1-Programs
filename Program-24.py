# Python Journal Program - Unit-1
# Definition : WAP TO CREATE DICTION DYNAMICALLY AND PERFORM UPDATE DEL AND ADD ACTION.
dict1 = {}
b = int(input("Total number of elements = "))
for i in range(1, b + 1):
    dict1[input("Enter Key for above element = ")] = input("Enter Element for key = ")
print(dict1)
key = input("Enter key to update = ")
value = input("Enter new value = ")
dict1.update({key: value})
dict1.pop(input("Enter Key to delete = "))
print(dict1)
dict1[input("Enter key for new value = ")] = input("Enter new value = ")
print(dict1)


"""
Output :
Total number of elements = 2
Enter Element for key = 1
Enter Key for above element = 1
Enter Element for key = 2
Enter Key for above element = 2
{'1': '1', '2': '2'}
Enter key to update = 1
Enter new value = 3
Enter Key to delete = 1
{'2': '2'}
Enter new value = 1
Enter key for new value = 1
{'2': '2', '1': '1'}
"""
