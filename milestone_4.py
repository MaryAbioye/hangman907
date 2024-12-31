# milestone_4.py

import random

# Step 1: Create the Hangman class
class Hangman:
    # Step 2: Define the __init__ method with word_list and num_lives as parameters
    def __init__(self, word_list, num_lives=5):
        # Step 3: Initialize the attributes
        self.word_list = word_list  # List of possible words
        self.num_lives = num_lives  # Number of lives the player has
        self.word = random.choice(self.word_list)  # Randomly select a word from the list
        self.word_guessed = ['_' for _ in self.word]  # List with _ for unguessed letters
        self.num_letters = len(set(self.word))  # Number of unique letters in the word
        self.list_of_guesses = []  # List to track the guesses already made

    # Step 2: Define the check_guess method
    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guess to lowercase
        
        # Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Create a for-loop that loops through each letter in the word
            for i, letter in enumerate(self.word):
                # If the letter matches the guess, replace the corresponding _ in word_guessed
                if letter == guess:
                    self.word_guessed[i] = guess

            # Reduce num_letters by 1 (one unique letter guessed correctly)
            self.num_letters -= 1
            
        else:
            # If the guess is not in the word, reduce lives and show messages
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
        self.display_game_state()  # Show updated game state

    # Step 3: Define the ask_for_input method
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")

            # Check if the guess is a valid single letter
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            # Check if the letter has already been guessed
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # If valid and not guessed before, process the guess
                self.check_guess(guess)
                self.list_of_guesses.append(guess)  # Add the guess to the list of guesses
                break  # Exit after a valid guess

    # Display current game state (for testing purposes)
    def display_game_state(self):
        print("Word to guess:", ' '.join(self.word_guessed))
        print(f"Lives remaining: {self.num_lives}")
        print(f"Guessed letters: {', '.join(self.list_of_guesses)}")

# Example usage:
if __name__ == "__main__":
    word_list = ["apple", "banana", "grape", "orange", "melon"]
    game = Hangman(word_list)  # Create a Hangman game instance
    game.ask_for_input()  # Ask the user to guess a letter