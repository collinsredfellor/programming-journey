"""
Number Guessing Game
Author: Collins Redfellor

The computer chooses a random number between 1 and 100.
The player keeps guessing until they find the correct number.
"""

import random


def generate_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)


def get_guess():
    """Ask the player for a valid number."""

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            return guess

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def give_hint(guess, secret_number):
    """Tell the player whether their guess is too high or too low."""

    if guess < secret_number:
        print("📉 Too low! Try again.")

    elif guess > secret_number:
        print("📈 Too high! Try again.")

    else:
        print("🎉 Correct! You guessed the number!")


def play_game():
    """Run one round of the guessing game."""

    secret_number = generate_number()
    attempts = 0

    print("\n" + "=" * 45)
    print("          🎯 NUMBER GUESSING GAME")
    print("=" * 45)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print("=" * 45)

    while True:
        guess = get_guess()
        attempts += 1

        give_hint(guess, secret_number)

        if guess == secret_number:
            print(f"\nYou got it in {attempts} attempt(s)! 🏆")
            break


def main():
    """Start and control the game."""

    print("\nWelcome to the Number Guessing Game!")

    while True:
        play_game()

        play_again = input(
            "\nWould you like to play again? (y/n): "
        ).strip().lower()

        if play_again != "y":
            print("\nThanks for playing! 👋")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
