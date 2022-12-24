# Python Journal Program - Unit-1
# Definition : CREATE A FUNCTION FOR ADD UPDATE AND DELETE DATA FROM THE DICTIONARY.

# Create A Dictionary
dict1 = {1: 'Python'}
print(dict1)

# Add new item
dict1[2] = 'Java'
print(dict1)

# Update the dictionary
dict1.update({3: 'JavaScript'})
print(dict1)

# Delete a specific element
del dict1[3]
print(dict1)

# Get the type of variable
print(type(dict1))

"""
Output :
{1: 'Python'}
{1: 'Python', 2: 'Java'}
{1: 'Python', 2: 'Java', 3: 'JavaScript'}
{1: 'Python', 2: 'Java'}
<class 'dict'>
"""
