# =========================================================
# Password Manager - Secure & User-Friendly
# =========================================================

import sys

class PasswordManager:
    def __init__(self, initial_master_password):
        self.passwords = {}  # Dictionary to store site credentials
        self.master_password = initial_master_password  # Master key for access

    def add_password(self, site, username, password):
        """Add a new password with validation (3-20 chars)."""
        if 3 <= len(password) <= 20:
            self.passwords[site] = {"username": username, "password": password}
            print(f"✅ Password for '{site}' added successfully!")
        else:
            print("❌ Password must be between 3 and 20 characters!")

    def get_password(self, site):
        """Retrieve a password after double master password verification."""
        # Two-step verification for security
        attempt1 = input("🔑 Enter master password to view: ")
        attempt2 = input("🔑 Confirm master password: ")
        
        if attempt1 == self.master_password and attempt2 == self.master_password:
            if site in self.passwords:
                data = self.passwords[site]
                print(f"\n🔓 Site: {site}")
                print(f"👤 Username: {data['username']}")
                print(f"🔐 Password: {data['password']}")
            else:
                print(f"❌ Site '{site}' not found!")
        else:
            print("❌ Access Denied: Wrong master password!")

    def delete_password(self, site):
        """Delete a password after double master password verification."""
        # Two-step verification for security
        attempt1 = input("🔑 Enter master password to delete: ")
        attempt2 = input("🔑 Confirm master password: ")

        if attempt1 == self.master_password and attempt2 == self.master_password:
            if site in self.passwords:
                del self.passwords[site]
                print(f"🗑️ Password for '{site}' deleted!")
            else:
                print(f"❌ Site '{site}' not found!")
        else:
            print("❌ Access Denied: Wrong master password!")

    def list_sites(self):
        """Display all saved sites with usernames."""
        if not self.passwords:
            print("📭 No passwords saved yet.")
        else:
            print("\n📋 Saved sites:")
            for site, data in self.passwords.items():
                print(f"- {site} (Username: {data['username']})")

    def change_master_password(self, old_password, new_password):
        """Change master password with old password confirmation."""
        if old_password != self.master_password:
            print("❌ Wrong master password!")
            return
        
        # Extra security: confirm old password again
        confirm_old = input("🔑 Please re-enter old master password to confirm: ")
        if confirm_old == self.master_password:
            self.master_password = new_password
            print("✅ Master password changed successfully!")
        else:
            print("❌ Confirmation failed! Master password not changed.")

# =========================================================
# USER INTERFACE
# =========================================================

def show_menu():
    """Display the main menu options."""
    print("\n" + "=" * 30)
    print("     🔐 PASSWORD MANAGER")
    print("=" * 30)
    print("1. Add Password")
    print("2. Get Password")
    print("3. Delete Password")
    print("4. List Sites")
    print("5. Change Master Password")
    print("6. Exit")
    print("=" * 30)

# =========================================================
# MAIN PROGRAM EXECUTION
# =========================================================

# Step 1: Set up master password on first run
first_pass = input("🔑 Set your initial master password: ")
pm = PasswordManager(first_pass)

# Step 2: Main application loop with authentication
while True:
    # Step 3: Require master password before showing menu
    auth_attempt = input("\n🔒 [LOCKED] Enter master password to access menu: ")
    if auth_attempt != pm.master_password:
        print("❌ Wrong password! Try again.")
        continue  # Go back to the beginning of the loop

    # Step 4: User is authenticated, show menu
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        site = input("🌐 Site: ")
        username = input("👤 Username: ")
        password = input("🔐 Password: ")
        pm.add_password(site, username, password)

    elif choice == "2":
        site = input("🌐 Site: ")
        pm.get_password(site)  # Double verification handled inside

    elif choice == "3":
        site = input("🌐 Site: ")
        pm.delete_password(site)  # Double verification handled inside

    elif choice == "4":
        pm.list_sites()

    elif choice == "5":
        old = input("🔑 Enter old master password: ")
        new = input("🔑 Enter new master password: ")
        pm.change_master_password(old, new)

    elif choice == "6":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option!")
        
# Developed By AmirHosseinKhani.py
# Email : amirsesemi6@gmail.com
# instagram : AmirHossein.py