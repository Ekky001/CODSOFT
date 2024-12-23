class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.\n")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
        print()

    def search_contact(self):
        search = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search in contact['name'] or search in contact['phone']]
        if not found_contacts:
            print("No contacts found.\n")
            return
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        print()

    def update_contact(self):
        search = input("Enter name or phone number of the contact to update: ")
        for contact in self.contacts:
            if search in contact['name'] or search in contact['phone']:
                print("Contact found. Enter new details (leave blank to keep current values):")
                name = input(f"Name [{contact['name']}]: ") or contact['name']
                phone = input(f"Phone [{contact['phone']}]: ") or contact['phone']
                email = input(f"Email [{contact['email']}]: ") or contact['email']
                address = input(f"Address [{contact['address']}]: ") or contact['address']
                contact.update({"name": name, "phone": phone, "email": email, "address": address})
                print("Contact updated successfully!\n")
                return
        print("Contact not found.\n")

    def delete_contact(self):
        search = input("Enter name or phone number of the contact to delete: ")
        for contact in self.contacts:
            if search in contact['name'] or search in contact['phone']:
                self.contacts.remove(contact)
                print("Contact deleted successfully!\n")
                return
        print("Contact not found.\n")

    def menu(self):
        while True:
            print("Contact Book")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
