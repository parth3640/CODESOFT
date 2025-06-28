contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Search by name or phone: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == keyword.lower() or contact["phone"] == keyword:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("No contact found.")

def update_contact():
    keyword = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == keyword.lower():
            print("Leave blank to keep existing value.")
            name = input(f"New name ({contact['name']}): ") or contact['name']
            phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New email ({contact['email']}): ") or contact['email']
            address = input(f"New address ({contact['address']}): ") or contact['address']

            contact.update({
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            })
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    keyword = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"].lower() == keyword.lower():
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()