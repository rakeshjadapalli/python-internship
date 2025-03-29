import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email (optional): ").strip()

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)

    print(f"\n✅ Contact '{name}' added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("\n⚠ No contacts found.")
        return
    
    print("\n📖 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact.get('email', 'No Email')}")

def search_contact():
    query = input("Enter name to search: ").strip().lower()
    contacts = load_contacts()
    results = [c for c in contacts if query in c["name"].lower()]

    if results:
        print("\n🔍 Search Results:")
        for contact in results:
            print(f"{contact['name']} - {contact['phone']} - {contact.get('email', 'No Email')}")
    else:
        print("\n⚠ No contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    contacts = load_contacts()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Editing {contact['name']}...")
            contact["phone"] = input(f"Enter new phone ({contact['phone']}): ") or contact["phone"]
            contact["email"] = input(f"Enter new email ({contact.get('email', 'No Email')}): ") or contact.get("email", "")
            save_contacts(contacts)
            print("\n✅ Contact updated successfully!")
            return

    print("\n⚠ Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    contacts = load_contacts()
    
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    
    if len(new_contacts) == len(contacts):
        print("\n⚠ Contact not found.")
    else:
        save_contacts(new_contacts)
        print(f"\n❌ Contact '{name}' deleted successfully!")

def main():
    while True:
        print("\n📞 Contact Book")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Update Contact")
        print("5️⃣ Delete Contact")
        print("6️⃣ Exit")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\n👋 Exiting Contact Book. Have a great day!")
            break
        else:
            print("\n⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
