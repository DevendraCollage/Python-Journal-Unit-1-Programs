# Python Journal Program - Unit-1
# Definition : WAP TO CREATE MENU DRIVEN PROGRAM.

# Create A Menu
while True:
    print("Menu Driven Program")
    print("1.Area Of Circle")
    print("2.Area Of Rectangle")
    print("3.Area Of Square")
    print("4.Exit")

    # Get the input from the user
    print("Enter Your Choice : ", end="")
    choice = int(input())

    # Print The Result user related Choice
    if choice == 1:
        print("Enter radius of circle : ", end="")
        radius = int(input())
        print("Area of Circle", 3.14 * radius * radius)

    elif choice == 2:
        print("Enter height of Rectangle : ", end="")
        height = int(input())
        print("Enter width of Rectangle : ", end="")
        width = int(input())
        print("Area of Rectangle :", height * width)

    elif choice == 3:
        print("Enter side of square : ", end="")
        side = int(input())
        print("Area :", side * side)

    elif choice == 4:
        break

    else:
        print("Wrong Choice")

    print("Do you want to continue? (Y/N)")
    repeat = input()
    if repeat == 'n' or repeat == 'N':
        break
    # If User Enter "Y" Then Repeat the loop
    # If User Enter "N" The Break The loop

# Output :
"""
Menu Driven Program
1.Area Of Circle
2.Area Of Rectangle
3.Area Of Square
4.Exit
Enter Your Choice : 3
Enter side of square : 4
Area : 16
Do you want to continue? (Y/N)
-> If you are enter "Y" then repeat the loop
-> If you are enter "N" then break the loop 
"""
