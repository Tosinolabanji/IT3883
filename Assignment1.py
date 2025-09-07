# Program Name: Assignment1.py
# Course: IT3883/ Section 01 (86369)
# Student Name: Tosin Olabanji
# Assignment Number: 
# Due Date: 09/06/2025
# Purpose: This program creates a text-based menu that allows the user to
#          append text to a buffer, clear the buffer, display the buffer,
#          or exit the program.
# Resources used: Basic Python syntax knowledge and practice examples.

# Start with option set to -1 so the loop will run
option = -1
# This variable will store the text entered by the user
words = ""

# Keep showing the menu until the user chooses option 4
while option != "4":
    # Display the menu options
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Ask the user to select an option
    option = input("please select a option")

    # If the user selects 1, append new text to the buffer
    if option == "1":
        words += input("Type a word")

    # If the user selects 2, clear the buffer
    elif option == "2":
        words = ""

    # If the user selects 3, display the buffer
    elif option == "3":
        print(words)

    # If the user selects 4, end the program
    elif option == "4":
        print("Program Ends")

    # Add a blank line for readability after each loop
    print()


