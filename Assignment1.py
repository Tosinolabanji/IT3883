	# Program Name: Assignment1.py (use the name the program is saved as)
	# Course: IT3883/ Section 01 (86369)
	# Student Name: Tosin Olabanji
	# Assignment Number: Lab#
	# Due Date: 09/06/ 2025
	# Purpose: What does the program do (in a few sentences)?
	# List Specific resources used to complete the assignment.
option=-1
words = ""
while option != "4":
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")
    option=input("please select a option")
    if option == "1":
        words += input("Type a word")
    elif option== "2":
        words = ""
    elif option== "3":
        print(words)
    elif option== "4":
        print("Program Ends")
    print()


