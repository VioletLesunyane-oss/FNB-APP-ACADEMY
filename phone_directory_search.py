# 1. Create a dictionary with 3 contacts
contacts = {
    "Mpho": "0821112222",
    "Dimpho": "0834567891",
    "Sarah": "0844313444"
}

# 2. Ask the user to enter a friend's name
name = input("Enter the name of the friend you want to look up: ")

# 3. Check if the name exists in the contacts dictionary
if name in contacts:

    # Get the phone number
    number = contacts[name]

    # Display the contact details
    print("Found!", name + "'s number is", number)

# 4. If the name does not exist
else:
    print("Contact not found.")