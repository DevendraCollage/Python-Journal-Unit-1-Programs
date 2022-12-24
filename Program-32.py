# Python Journal Program - Unit-1
# Definition : CREATE A FUNCTION FOR ADD UPDATE AND DELETE DATA FROM THE LIST.

# Create A List
list1 = ["Dell", "HP", "Lenovo", "Asus", "Acer"]
print(list1)

# Add the item in the list
list1.append("Samsung")
print(list1)

# Update the item in the list
list1.insert(1, "Samsung")
print(list1)

# Delete item from the list
list1.remove("Samsung")
print(list1)

# Get the type of the variable
print(type(list1))


# Output :
"""
['Dell', 'HP', 'Lenovo', 'Asus', 'Acer'] - Create only List
['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Samsung'] - Add item at the end of the list
['Dell', 'Samsung', 'HP', 'Lenovo', 'Asus', 'Acer', 'Samsung'] - Update the item at specific position in the list
['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Samsung'] - Delete the item from the list
<class 'list'> - show the type of the variable
"""