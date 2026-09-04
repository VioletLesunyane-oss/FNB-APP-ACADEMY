# In Python every letter is called a string. A string is a sequence of characters enclosed 
# in either single quotes (' ') or double quotes (" "). Strings can contain letters, numbers, symbols, and whitespace.
# Python doesn't see a string as a one single block, instead it sees it as multiple charecters chained together.
# The Golden rule in Python is that we start counting from 0, meaning the first letter of a string is at position 0, 
# the second letter is at position 1, and so on.
# Tracking individual letters
#name = "Python"

#print(name[0])  # Output: P
# Note: We use [] to access a specific letter in a string, and the number inside the brackets is the position of the letter 
# we want to access.
# -1 is the shortest way of countin from the end of a string, meaning the last letter of a string is at position -1(n), 
# the second last letter is at position -2(o), and so on.
#print(name[-1])  # Output: n
#print(name[2])  # Output: t
#print(name[3])  # Output: h
#print(name[4])  # Output: o
#print(name[5])  # Output: n
 
 # using the string methods to manipulate strings
 # Note: A method is called using dot notation (.)
 # List of string methods:
 # .upper() - converts the string to uppercase
 # .strip() - removes whitespace from the beginning and end of the string
 # .lower() - converts the string to lowercase
 # Below example: town(variable) and " Johannesburg " (string/value). A string is stored in a variable
 # When accesing a string we use e.g .upper() method to convert the string to uppercase, .strip() method to remove whitespace 
 # from the beginning and end of the string, and .lower() method to convert the string to lowercase.

#town = " Johannesburg "

#print(town.upper())  # Output:   JOHANNESBURG  # with whitespace
#print(town.strip())  # Output: Johannesburg
#print(town.lower())  # Output: johannesburg

# Creating a professional system email generator
# To achieve this we will be asking the user to input their first name and last_name, 
# then we will use the f-string method to manipulate the strings and create a professional system email.
# Note: The .strip() method is used to remove any whitespace incase the user accidentally adds whitespace before or after 
# their name.
first = input("Enter your first name: ").strip()
last= input("Enter your last name: ").strip()

username = f"{first[0]}{last}" # This is an f-string that combines the first letter of the first name and the last name to 
#create a username.
print(f"Your email is : {username.lower()}@university.co.za") # This is an f-string that combines the username and the domain 
# name to create a professional system email.
# In the terminal, the user will be prompted to enter their first name and last name, and the program will output their professional system email.
# Output would be: Enter your first name:   Violet
#Enter your last name: Lesunyane
#Your email is : vlesunyane@university.co.za