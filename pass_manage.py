# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:53:50 2023

@author: Sudipta
"""

import hashlib
import getpass

passwords = {}

def get_hashed_password(password):
    """Generate a SHA-256 hashed password."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

def create_password():
    """Create a new password entry."""
    website = input("Enter the website: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = get_hashed_password(password)
    passwords[website] = (username, hashed_password)
    print("Password created successfully.")

def retrieve_password():
    """Retrieve a password from the password manager."""
    website = input("Enter the website: ")
    if website in passwords:
        username, hashed_password = passwords[website]
        password = getpass.getpass("Enter your password: ")
        if hashed_password == get_hashed_password(password):
            print(f"Username: {username}")
            print(f"Password: {password}")
        else:
            print("Incorrect password.")
    else:
        print("Website not found in the password manager.")

def main():
    while True:
        print("1. Create a new password")
        print("2. Retrieve a password")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            create_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()