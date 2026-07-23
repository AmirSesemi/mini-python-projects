# Contacts App
# This program helps you manage your contacts efficiently.

# Main list to store all contacts
contacts = []

# Dictionary for grouping contacts
groups = {"Family": [], "Friends": [], "Work": [], "Other": []}

# Set to keep track of valid group names for input validation
group_names = {"Family", "Friends", "Work", "Other"}

while True:
    # Display menu
    print("\n" + "=" * 30)
    print("   Contacts App")
    print("=" * 30)
    print("1. Add Contact")
    print("2. View All Contacts")   
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. View Contacts by Group")
    print("6. Show All Groups")
    print("7. Exit")
    print("=" * 30)

    choice = input("Choose an option: ")

    if choice == "1":
        print("Add Contact")
        
        # Get contact details from user
        contact_name = input("Contact Name: ")
        
        # Validate phone number (3-12 digits, only numbers)
        while True:
            contact_number = input("Phone Number (3-12 digits): ")
            if contact_number.isdigit() and 3 <= len(contact_number) <= 12:
                break
            elif not contact_number.isdigit():
                print("Please enter only numbers!")
            else:
                print("Phone number must be between 3 and 12 digits!")
        
        contact_email = input("Email: ")
        
        # Validate group (must be one of the valid groups)
        while True:
            contact_group = input("Group (Family/Friends/Work/Other): ")
            if contact_group in group_names:
                break
            else:
                print("Please enter a valid group name!")

        # Create contact (TUPLE) and store it
        contact = (contact_name, contact_number, contact_email, contact_group)
        contacts.append(contact)  # Store in main list
        groups[contact_group].append(contact)  # Store in specific group
        print("New contact added successfully!")

    elif choice == "2":
        print("View Contacts")
        if not contacts:
            print("No contacts found!")
        else:
            # Loop to display all contacts
            for contact in contacts:
                name, phone, email, group = contact
                print(f"Name: {name}, Phone: {phone}, Email: {email}, Group: {group}")

    elif choice == "3":
        print("Search")
        search_term = input("Name or Phone: ")
        found = False
        # Loop to search for contacts
        for contact in contacts:
            name, phone, email, group = contact
            if search_term.lower() in name.lower() or search_term in phone:
                print(f"Found: {name}, {phone}, {email}, {group}")
                found = True
        if not found:
            print("Contact not found!")

    elif choice == "4":
        print("Delete Contact")
        del_name = input("Name of contact to delete: ")
        found = False
        # Loop to find and delete contact
        for contact in contacts:
            name, phone, email, group = contact
            if name == del_name:
                contacts.remove(contact)  # Delete from main list
                if contact in groups[group]:
                    groups[group].remove(contact)  # Delete from specific group
                print("Contact deleted successfully.")
                found = True
                break
        if not found:
            print("Contact not found!")

    elif choice == "5":
        print("View Contacts by Group")
        view_contact_group = input(
            "Enter group name (Family/Friends/Work/Other): "
        )
        if view_contact_group not in group_names:
            print("Please enter a valid group name!")
        else:
            # Get contacts from selected group from dictionary
            group_contacts = groups.get(view_contact_group, [])
            if not group_contacts:
                print("This group has no contacts!")
            else:
                # Display contacts in the group
                for contact in group_contacts:
                    name, phone, email, group = contact
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")

    elif choice == "6":
        print("Groups:")
        # Display all valid group names
        for group in group_names:
            print(f"- {group}")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Please enter a number from 1 to 7!")


# Developed By AmirHosseinKhani.py
# Email : amirsesemi6@gmail.com
# instagram : AmirHosseinKhani.py
