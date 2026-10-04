"""
Strong Password Generator
Author: Collins Redfellor

A beginner-friendly password generator that creates
strong random passwords.

Features:
- Custom password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Secure random generation
"""

import secrets
import string


def get_password_length():
    """Ask the user for a valid password length."""

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password must be at least 8 characters long.")
                continue

            return length

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def generate_password(length):
    """Generate a strong random password."""

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+[]{}<>?/"

    # Make sure the password contains at least
    # one character from each category.
    password_characters = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    all_characters = uppercase + lowercase + numbers + symbols

    # Fill the remaining password characters.
    for _ in range(length - 4):
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Securely shuffle the password.
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def main():
    """Start the password generator."""

    print("\n" + "=" * 50)
    print("           🔐 STRONG PASSWORD GENERATOR")
    print("=" * 50)

    print("\nCreate a strong password for your account.")
    print("Your password will contain:")
    print("- Uppercase letters")
    print("- Lowercase letters")
    print("- Numbers")
    print("- Special characters")

    print()

    length = get_password_length()
    password = generate_password(length)

    print("\n" + "=" * 50)
    print("             YOUR STRONG PASSWORD")
    print("=" * 50)
    print(password)
    print("=" * 50)

    print("\n⚠️ Keep your password private.")
    print("Do not share it with other people.")


if __name__ == "__main__":
    main()
