import random

# Define a list of possible secret words
secret_words = ["apple", "banana", "grape", "orange", "melon"]

# Randomly choose a secret word
secret_word = random.choice(secret_words)

# Define the check_guess function
def check_guess(guess):
    # Convert the guess to lower case
    guess = guess.lower()

    # Check if the guess is in the secret word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Define the ask_for_input function
def ask_for_input():
    while True:
        # Ask the user to guess a letter
        guess = input("Please guess a letter: ")

        # Check if the guess is a single alphabetical character
        if guess.isalpha() and len(guess) == 1:
            # Call the check_guess function and pass the guess as an argument
            check_guess(guess)
            break  # Exit the loop after a valid guess
        else:
            # If the guess is invalid, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call the ask_for_input function to test the code
ask_for_input()
