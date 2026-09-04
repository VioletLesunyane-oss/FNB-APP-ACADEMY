# 1. Create a formatted string using the input values
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
#bio = input("Enter a short bio about yourself: ")

# 2. Create a username by combining first initial + last name in lowercase (e.g. tdlamini)
#first_name = 'Violet'
#last_name = 'Lesunyane'
#username = f"{first_name[0].lower()}{last_name.lower()}"
#print(f"Your username is: {username}")

# 3. Display the full name in Title Case using .title()
#full_name = 'violet lesunyane'
#print(full_name.title())

# 4. Strip leading/trailing whitespace from the bio before displaying it using .strip()
#bio = "    I am 39 years old from hammanskraal.  "
#print(bio.strip())

# 5. Count the number of characters in the bio using len()
#bio = "I am 39 years old from hammanskraal."
#print(len(bio))

# 6. Replace any occurance of 'I am' in the bio with 'I'm' using .replace()
#bio = "I am 39 years old from hammanskraal."
#print(bio.replace("I am", "I'm"))

# 7. Display all output using f-strings
#7.1
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
#bio = input("Enter a short bio about yourself: ")
#print(f"Name: {first_name} {last_name}\nBio: {bio}")

#7.2
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
#username = f"{first_name[0].lower()}{last_name.lower()}"
#print(f"Your username is: {username}")

#7,3
#full_name = 'violet lesunyane'
#print(f"Name: {full_name.title()}")

#7.4
#full_name = 'Violet' 
#last_name = 'Lesunyane'
#age = 39
#location = "Hammanskraal"
#print(f"My name is {full_name} {last_name}, i am {age} years old from {location.lower()}")

#7.4
#bio = "    I am 39 years old from hammanskraal.  "
#print(f"Stripped Bio: {bio.strip()}")

#7.5
#bio = "I am 39 years old from hammanskraal."
#print(f"Total number of characters: {len(bio)}")

#7.6
bio = "I am 39 years old from hammanskraal."
print(f"Updated Bio: {bio.replace('I am', 'I\'m')}")
