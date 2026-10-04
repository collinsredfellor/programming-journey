"""
Authentication and Login System
Author: Collins Redfellor

A beginner-friendly console authentication system.

Features:
- User registration
- Login
- Password hashing
- Multiple users
- Logout
- Input validation

Note:
This is an educational project.
It is NOT intended for production authentication.
"""

import hashlib
import getpass


# Store registered users.
# In this beginner project, users are stored in memory.
users = {}


def hash_password(password):
    """
    Convert a password into a secure hash.

    The original password is never stored directly.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user():
    """Register a new user."""

    print("\n" + "=" * 45)
    print("             USER REGISTRATION")
    print("=" * 45)

    username = input("Enter a username: ").strip()

    if not username:
        print("Error: Username cannot be empty.")
        return

    if username in users:
        print("Error: Username already exists.")
        return

    password = getpass.getpass("Enter a password: ")

    if len(password) < 6:
        print("Error: Password must contain at least 6 characters.")
        return

    confirm_password = getpass.getpass("Confirm your password: ")

    if password != confirm_password:
        print("Error: Passwords do not match.")
        return

    password_hash = hash_password(password)

    users[username] = {
        "password": password_hash
    }

    print("\nRegistration successful! ✅")
    print(f"Welcome, {username}!")


def login_user():
    """Log a user into the system."""

    print("\n" + "=" * 45)
    print("                USER LOGIN")
    print("=" * 45)

    username = input("Username: ").strip()

    if username not in users:
        print("Error: Username or password is incorrect.")
        return None

    password = getpass.getpass("Password: ")

    password_hash = hash_password(password)

    if password_hash == users[username]["password"]:
        print("\nLogin successful! 🔓")
        print(f"Welcome back, {username}!")

        return username

    print("Error: Username or password is incorrect.")
    return None


def user_dashboard(username):
    """Display the dashboard for a logged-in user."""

    while True:
        print("\n" + "=" * 45)
        print("              USER DASHBOARD")
        print("=" * 45)
        print(f"Logged in as: {username}")
        print("\n1. View profile")
        print("2. Logout")
        print("=" * 45)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\n" + "-" * 45)
            print("PROFILE")
            print("-" * 45)
            print(f"Username: {username}")
            print("Account status: Active")
            print("-" * 45)

        elif choice == "2":
            print(f"\nGoodbye, {username}! 👋")
            return

        else:
            print("\nInvalid choice. Please choose 1 or 2.")


def main_menu():
    """Display the main authentication menu."""

    while True:
        print("\n" + "=" * 45)
        print("        PYTHON AUTHENTICATION SYSTEM")
        print("=" * 45)
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("=" * 45)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            username = login_user()

            if username:
                user_dashboard(username)

        elif choice == "3":
            print("\nThank you for using the system.")
            print("Goodbye! 👋")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


def main():
    """Start the authentication system."""

    print("\n🔐 Welcome to the Python Authentication System!")

    try:
        main_menu()

    except (EOFError, OSError):
        print("\nThis environment does not support interactive input.")
        print("The program should be run in a normal Python terminal.")


if __name__ == "__main__":
    main()
