# Number Guessing Game
# Beginner project: Python functions + loops + random
#
# The computer thinks of a secret number.
# You guess it, and after every guess you get a hint (higher / lower).

import random


def choose_difficulty():
    """Ask the user to choose a difficulty.
    Returns: (biggest number, number of guesses allowed)"""
    print("\nChoose a difficulty:")
    print("1. Easy   (1 to 10,  5 guesses)")
    print("2. Medium (1 to 50,  7 guesses)")
    print("3. Hard   (1 to 100, 7 guesses)")

    while True:
        choice = input("Option (1-3): ")
        if choice == "1":
            return 10, 5
        elif choice == "2":
            return 50, 7
        elif choice == "3":
            return 100, 7
        print("Invalid option! Type 1, 2 or 3.")


def get_guess(max_number):
    """Ask the user for a guess. Ask again if the input is wrong."""
    while True:
        text = input("Your guess: ")
        try:
            guess = int(text)
        except ValueError:
            print("Please enter a number, like 25.")
            continue

        if guess < 1 or guess > max_number:
            print(f"The number must be between 1 and {max_number}.")
            continue

        return guess


def play_round():
    """Play one full game. Returns True if the user won."""
    max_number, max_attempts = choose_difficulty()
    secret = random.randint(1, max_number)

    print(f"\nI am thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} guesses. Good luck!")

    for attempt in range(1, max_attempts + 1):
        print(f"\nGuess {attempt} of {max_attempts}")
        guess = get_guess(max_number)

        if guess == secret:
            print(f"Well done! That is correct, the number was {secret}.")
            print(f"You won in {attempt} guesses!")
            return True
        elif guess < secret:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")

    print(f"\nYou are out of guesses! The number was {secret}.")
    return False


def ask_play_again():
    """Return True if the user wants to play again."""
    while True:
        answer = input("\nPlay again? (y/n): ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        print("Please type y or n.")


def main():
    print("=== Number Guessing Game ===")
    wins = 0
    games = 0

    while True:
        games += 1
        if play_round():
            wins += 1

        print(f"Score: {wins} wins out of {games} games")

        if not ask_play_again():
            print("Goodbye!")
            break


# The program starts here
main()
