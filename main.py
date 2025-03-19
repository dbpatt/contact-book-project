class Contact:
    """Defines a contact with name, phone, and email. Used as a node in the linked list."""
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None  # Pointer to the next contact (for linked list)


class ContactBook:
    """Manages contacts using a Linked List (for ordering) and a Hash Table (for fast lookups)."""
    def __init__(self):
        self.contacts = {}  # Hash Table for quick access
        self.head = None  # Head of the linked list


    def add_contact(self, name, phone, email):
        """Adds a new contact. Uses hash table for lookup and inserts into linked list in sorted order."""
        # Check if the contact already exists
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
            return

        # Validate inputs (basic example)
        if not name or not phone or not email:
            print("Error: Name, phone, and email cannot be empty.")
            return

        # Create a new contact
        new_contact = Contact(name, phone, email)
        self.contacts[name] = new_contact  # Store in Hash Table

        # Insert in Linked List (Alphabetical Order, Case-Insensitive)
        if not self.head or name.lower() < self.head.name.lower():
            new_contact.next = self.head
            self.head = new_contact
        else:
            current = self.head
            while current.next and current.next.name.lower() < name.lower():
                current = current.next
            new_contact.next = current.next
            current.next = new_contact

        print(f"Added: {name}")


    def search_contact(self, name):
        """Searches for a contact using the Hash Table (O(1) time complexity)."""
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Found: {contact.name} | {contact.phone} | {contact.email}")
            return contact
        print(f"Contact '{name}' not found.")
        return None


    def delete_contact(self, name):
        """Deletes a contact from both the Hash Table and Linked List."""
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return

        # Remove from Hash Table
        del self.contacts[name]

        # Remove from Linked List
        if self.head.name == name:
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.name != name:
                current = current.next
            if current.next:
                current.next = current.next.next

        print(f"Deleted: {name}")


    def display_contacts(self):
        """Prints all contacts in alphabetical order (linked list traversal)."""
        current = self.head
        if not current:
            print("Contact book is empty.")
            return
        print("Contacts:")
        while current:
            print(f"{current.name} | {current.phone} | {current.email}")
            current = current.next


    def update_contact(self, name, phone=None, email=None):
        """Updates a contact's phone number or email."""
        if name not in self.contacts:
            print(f"Contact '{name}' not found.")
            return

        contact = self.contacts[name]
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        print(f"Updated: {name} | {contact.phone} | {contact.email}")
