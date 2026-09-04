## CONTACT BOOK DICTIONERY
#Python dictioneries allows us to work with Key value pairs
# Key value pairs link values where the key is a unique identifier where we can find data and th value is that data
#Think of it like a real physical dictionery where we look up what would be the key and
# the definition of that word would be the value
#Example: {key:value}

# CONTACT BOOK

# Store contacts in a list
contact_list = []


# 1. Add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contact_list.append(contact)

    print("Contact added successfully!")


# 2. Search for a contact
def search_contact(name):
    for contact in contact_list:
        if contact["name"] == name:
            return contact

    return None


# 3. Delete a contact
def delete_contact(name):
    for contact in contact_list:
        if contact["name"] == name:
            contact_list.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


# 4. View all contacts
def view_all():
    if len(contact_list) == 0:
        print("No contacts found.")
    else:
        for contact in contact_list:
            print("--------------------")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        print("--------------------")


# 5. Menu
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        name = input("Enter name to search: ")
        result = search_contact(name)

        if result:
            print("Contact found!")
            print(f"Name: {result['name']}")
            print(f"Phone: {result['phone']}")
            print(f"Email: {result['email']}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_all()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1-5.")


