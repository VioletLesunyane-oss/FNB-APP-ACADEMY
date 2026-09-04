# The secure password hint tool 
# is a simple command-line application that helps users create secure password hints. 
# It takes a password as input and generates a hint that is easy to remember but difficult for others to guess.

#1. Ask the user to input their secret password.
#password = input("Enter your password: ")

#2 Clean up the password by removing any leading or trailing whitespace using .strip() method.
#print(password.strip())

#3.Grab the very first letter and the very last letter of the password using indexing.

#first_letter = password[0]
#last_letter = password[-1]

#4. Print a hint using f-string that forces the letters into uppercase.
#print(f"Your password hint: Starts with {first_letter.upper()} and ends with {last_letter.upper()}")

full_name = 'violet lesunyane'
print(full_name.title())


