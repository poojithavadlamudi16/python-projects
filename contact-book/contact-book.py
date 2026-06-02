# Contact Book

contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")

        else:
            print("\n--- Contact List ---")
            for contact in contacts:
                print("\nName :", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif choice == "3":
        search = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == search.lower():
                print("\nContact Found")
                print("Name :", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "4":
        search = input("Enter name to update: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == search.lower():

                contact["phone"] = input("Enter new phone number: ")
                contact["email"] = input("Enter new email: ")

                print("Contact updated successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        search = input("Enter name to delete: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == search.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")