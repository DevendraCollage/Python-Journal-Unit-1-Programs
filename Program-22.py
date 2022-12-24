# Python Journal Program - Unit-1
# Definition : WAP TO CREATE DYNAMIC LIST AND PRINT ALL NUMBER WITH POSITION ( USE len( ) TO FIND LENGTH. )
dict1 = {}
list1 = [['a', 1], ['b', 2], ['c', 3], ['d', 4]]
print("Empty Dictionary :", dict1)
for i in range(len(list1)):
    if list1[i][0] in dict1.keys():
        dict1[list1[i][0].append(list1[i][1])]
    else:
        dict1[list[i][1]] = []
        dict1[i][0].append(list1[i][1])
print("After Append : ", dict1)
dict1.update(d=[2])
print("After Update : ", dict1)
dict1.pop('b')
print("After Delete :", dict1)

"""
Output :
"""