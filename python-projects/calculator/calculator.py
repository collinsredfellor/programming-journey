"""
Simple Python Calculator
Author: Collins Redfellor
Description:
    A beginner-friendly command-line calculator
    that performs basic arithmetic operations.
"""


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference between two numbers."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Return the result of dividing two numbers."""
    if second_number == 0:
        return "Error: Cannot divide by zero."

    return first_number / second_number


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print("          PYTHON CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 40)


def get_numbers():
    """Ask the user for two numbers."""
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))

            return first_number, second_number

        except ValueError:
            print("\nInvalid input. Please enter numbers only.")


def main():
    """Run the calculator program."""

    print("\nWelcome to the Python Calculator!")

    while True:
        display_menu()

        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the Python Calculator!")
            print("Goodbye! 👋")
            break

        if choice not in ("1", "2", "3", "4"):
            print("\nInvalid choice. Please select an option from 1 to 5.")
            continue

        first_number, second_number = get_numbers()

        if choice == "1":
            result = add(first_number, second_number)
            operation = "+"

        elif choice == "2":
            result = subtract(first_number, second_number)
            operation = "-"

        elif choice == "3":
            result = multiply(first_number, second_number)
            operation = "*"

        else:
            result = divide(first_number, second_number)
            operation = "/"

        print("\n" + "-" * 40)
        print(f"Calculation: {first_number:g} {operation} {second_number:g}")
        print(f"Result: {result}")
        print("-" * 40)


if __name__ == "__main__":
    main()
