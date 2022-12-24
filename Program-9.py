# Python Journal Program - Unit-1
# Definition : WAP TO GET VALUE FROM THE USER AND PRINT MARK-SHEET.

# Get the 5 subject marks from the user
print("-- Enter Your 5 Subject Marks --")
print("Maths : ", end="")
maths = int(input())
print("English : ", end="")
english = int(input())
print("Physics : ", end="")
physics = int(input())
print("Biology : ", end="")
biology = int(input())
print("Science : ", end="")
science = int(input())

# Calculate the Total and Percentage
total = maths + english + physics + biology + science
print("Your Total Is : ", total)
percentage = total / 5
print("Your Percentage Is : ", percentage)

# Calculate the grade
if percentage >= 90:
    print("You Grade Is A")
elif percentage >= 80 and percentage < 90:
    print("Your Grade Is B")
elif percentage >= 70 and percentage < 80:
    print("Your Grade Is C")
elif percentage >= 60 and percentage < 70:
    print("Your Grade Is D")
elif percentage >= 50 and percentage < 60:
    print("Your Grade Is E")
else:
    print("Fail")


# Output :
"""
-- Enter Your 5 Subject Marks --
Maths : 40
English : 50
Physics : 60
Biology : 70
Science : 80
Your Total Is : 300
Your Percentage Is : 60.0
Your Grade Is : D 
"""