# milestone_3.py

import random

# Step 1: Define a list of possible secret words
secret_words = ["apple", "banana", "grape", "orange", "melon"]

# Step 2: Randomly choose a secret word
secret_word = random.choice(secret_words)

# Step 3: Define the check_guess function
def check_guess(guess):
    # Step 2: Convert the guess to lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the secret word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 4: Define the ask_for_input function
def ask_for_input():
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Please guess a letter: ")

        # Step 3: Check if the guess is a single alphabetical character
        if guess.isalpha() and len(guess) == 1:
            # Step 4: Call the check_guess function and pass the guess as an argument
            check_guess(guess)
            break  # Exit the loop after a valid guess
        else:
            # Step 5: If the guess is invalid, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 5: Call the ask_for_input function to test the code
ask_for_input()
