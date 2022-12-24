# Python Journal Program - Unit-1
# Definition : WAP TO CREATE A FILE AND WRITE TEXT INTO THE FILE.
# This program shows how to write data in a text file.

# Create the file
file = open("demo.txt", "w")
# Add the Multiple Strings in the file
L = ["Hello My Name is Devendra \n",
     "This is Python Create File And Insert String into the file Program \n",
     "This is the file-handling in python \n"]

# This function add the string at the single line
file.write("Hello There \n")
# This function is add multiple string in the file same time
file.writelines(L)
# This function end the file - this function tells to the python interpreter to end of the file
file.close()


# Output :
"""
Create the text file and add the string : demo.txt
Hello There
Hello My Name is Devendra
This is Python Create File And Insert into the file Program
This is the file-handling in python
"""
