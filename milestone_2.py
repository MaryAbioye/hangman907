#MILESTONE 1
# import Library
import random

# Create a list containing the names of your 5 favorite fruits
word_list = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# Print out the newly created list
print(word_list)

# Use the random.choice method and pass the word_list variable
word = random.choice (word_list)

# print the random word
print(word)

#input a guess letter
guess = input('Enter a single leter')

# print out the result
print (guess)

# create a condition for the length of the variable
if len(guess) == 1 and guess.isalpha():

# print a message if the input is valid
    print("Good guess!")
else:
# print a message if the input is invalid
  print ("Oops! That is not a valid input." )

#MILESTONE 2
# import random

# define a function to create list of fruits
def create_favourite_fruits ():
   return ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# funtion to create random word from a list
def get_random_word(word_list):
    return random.choice(word_list)

#function to validate the users guess
def validate_guess(guess):
  if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
  else:
        print("Oops! That is not a valid input.")


# Main program flow
def main():
    # Create the list of favorite fruits
    favorite_fruits = create_favourite_fruits
    print("Favorite Fruits:", favorite_fruits)

    # Get a random word
    random_word = get_random_word(favorite_fruits)
    print("Random Word:", random_word)

    # Get user input for a guess
    user_guess = input('Enter a single letter: ')
    print("Your Guess:", user_guess)

    # Validate the user's guess
    validate_guess(user_guess)

# Run the program
if __name__ == "__main__":
    main()

#MILESTONE 3

while True:
    # Step 2: Ask the user to guess a letter
    guess = input("Guess a letter: ")

    # Step 3: Check if the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        print("Valid guess!")
        # Step 4: Break out of the loop if the guess is valid
        break
    else:
        # Step 5: Print an error message if the guess is invalid
        print("Invalid letter. Please, enter a single alphabetical character.")

import random

# List of possible secret words
word_list = ["apple", "banana", "grape", "orange", "mango"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Step 1: Loop to continuously ask for a valid guess
while True:
    # Step 2: Ask the user to guess a letter
    guess = input("Guess a letter: ")

    # Step 3: Check if the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # Step 4: Check if the guessed letter is in the secret word
        if guess.lower() in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            break  # Exit the loop after a valid guess
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
    else:
        # Step 5: Print an error message if the guess is invalid
        print("Invalid letter. Please, enter a single alphabetical character.")

import random
#MILESTONE 4

# List of possible secret words
word_list = ["apple", "banana", "grape", "orange", "mango"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Step 1: Define the check_guess function
def check_guess(guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
        return True  # Return True if guess is correct
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False  # Return False if guess is incorrect

# Step 4: Define the ask_for_input function
def ask_for_input():
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Guess a letter: ")

        # Step 3: Validate the input (it must be a single alphabetical character)
        if len(guess) == 1 and guess.isalpha():
            # Call check_guess function to validate the guess
            if check_guess(guess):
                break  # Exit the loop if the guess is correct
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 5: Outside the function, call ask_for_input to test the code
ask_for_input()

# Function to check if the guess is in the secret word
def validate_and_check_guess(guess, secret_word):
    """Check if the guessed letter is in the secret word."""
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Function to prompt the user for input
def prompt_user_for_input(secret_word):
    """Continuously prompt the user for valid input and check the guess."""
    while True:
        guess = input("Enter a single letter: ").strip()
        if len(guess) == 1 and guess.isalpha():
            validate_and_check_guess(guess, secret_word)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Main execution
if __name__ == "__main__":
    # List of words and selecting a random word
    words_list = ["apple", "banana", "mango", "orange", "grape"]
    secret_word = random.choice(words_list)
    
    print("Welcome to the Word Guessing Game!")
    prompt_user_for_input(secret_word)

    class Hangman:
    """A class representing the Hangman game."""

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with the given word list and number of lives.

        Attributes:
            word (str): The word to be guessed, randomly selected from the word list.
            word_guessed (list): A list representing the letters guessed so far with '_' for unguessed letters.
            num_letters (int): The number of unique letters in the word that have not been guessed yet.
            num_lives (int): The number of lives the player has remaining.
            word_list (list): The list of words from which the word is chosen.
            list_of_guesses (list): A list to track letters that have already been guessed.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  # Unique letters in the word
        self.list_of_guesses = []

# Test the class
if __name__ == "__main__":
    # Test data
    words = ["apple", "banana", "grape", "orange", "mango"]
    game = Hangman(words)

    print(f"Word to guess: {''.join(game.word)}")  # For testing purposes
    print(f"Word guessed: {game.word_guessed}")
    print(f"Number of unique letters: {game.num_letters}")
    print(f"Lives: {game.num_lives}")
    print(f"Word list: {game.word_list}")
    print(f"List of guesses: {game.list_of_guesses}")

def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Args:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Update word_guessed and decrement num_letters
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1

def ask_for_input(self):
        """Continuously prompt the user for a valid guess and check it against the word."""
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Test the class
if __name__ == "__main__":
    # Test data
    words = ["apple", "banana", "grape", "orange", "mango"]
    game = Hangman(words)

    # Test the game by calling ask_for_input
    game.ask_for_input()
    print(f"Word guessed so far: {''.join(game.word_guessed)}")
    print(f"Lives remaining: {game.num_lives}")
    print(f"Guesses so far: {game.list_of_guesses}")

    def check_guess(self, guess):
        guess = guess.lower()
    if guess in self.word:
        print(f"Good guess! {guess} is in the word.")
        # Update word_guessed with the correct guess
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess
        # Decrement num_letters by 1 for each unique letter guessed
        self.num_letters -= 1
    else:
        print(f"Sorry, {guess} is not in the word.")
        self.num_lives -= 1
        

def check_guess(self, guess):
    """
    Check if the guessed letter is in the word and update word_guessed accordingly.

    Args:
        guess (str): The letter guessed by the player.
    """
    guess = guess.lower()
    if guess in self.word:
        print(f"Good guess! {guess} is in the word.")
        # Update word_guessed with the correct guess
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess
        # Decrement num_letters by 1 for each unique letter guessed
        self.num_letters -= 1
    else:
        # Handle incorrect guesses
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

   
class Hangman:
    """A class representing the Hangman game."""

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with the given word list and number of lives.

        Attributes:
            word (str): The word to be guessed, randomly selected from the word list.
            word_guessed (list): A list representing the letters guessed so far with '_' for unguessed letters.
            num_letters (int): The number of unique letters in the word that have not been guessed yet.
            num_lives (int): The number of lives the player has remaining.
            word_list (list): The list of words from which the word is chosen.
            list_of_guesses (list): A list to track letters that have already been guessed.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  # Unique letters in the word
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word and update word_guessed accordingly.

        Args:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Update word_guessed with the correct guess
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            # Decrement num_letters by 1 for each unique letter guessed
            self.num_letters -= 1
        else:
            # Handle incorrect guesses
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Continuously prompt the user for a valid guess and check it against the word."""
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Test the class
if __name__ == "__main__":
    # Test data
    words = ["apple", "banana", "grape", "orange", "mango"]
    game = Hangman(words)

    # Test the game by calling ask_for_input
    game.ask_for_input()
    print(f"Word guessed so far: {''.join(game.word_guessed)}")
    print(f"Lives remaining: {game.num_lives}")
    print(f"Guesses so far: {game.list_of_guesses}")

import random

class Hangman:
    """A class to represent the Hangman game."""

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.
        """
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def validate_guess(self, user_guess):
        """
        Check if the guessed letter is in the word.
        """
        user_guess = user_guess.lower()
        if user_guess in self.word:
            for index, letter in enumerate(self.word):
                if letter == user_guess:
                    self.word_guessed[index] = user_guess
            self.num_letters -= 1
            print(f"Good guess! {user_guess} is in the word.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {user_guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def get_user_input(self):
        """
        Ask the user for input and validate it.
        """
        while True:
            user_guess = input("Enter a single letter: ")
            if not user_guess.isalpha() or len(user_guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(user_guess)
                self.validate_guess(user_guess)
                break

# Milestone 5


class Hangman:
    """A class to represent the Hangman game."""

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.
        """
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def validate_guess(self, user_guess):
        """
        Check if the guessed letter is in the word.
        """
        user_guess = user_guess.lower()
        if user_guess in self.word:
            for index, letter in enumerate(self.word):
                if letter == user_guess:
                    self.word_guessed[index] = user_guess
            self.num_letters -= 1
            print(f"Good guess! {user_guess} is in the word.")
            print("Current word progress:", " ".join(self.word_guessed))
        else:
            self.num_lives -= 1
            print(f"Sorry, {user_guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def get_user_input(self):
        """
        Ask the user for input and validate it.
        """
        while True:
            user_guess = input("Enter a single letter: ")
            if not user_guess.isalpha() or len(user_guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(user_guess)
                self.validate_guess(user_guess)
                break

def play_game(word_list):
    """
    Function to run the Hangman game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost! The word was:", game.word)
            break
        elif game.num_letters > 0:
            game.get_user_input()
        else:
            print("Congratulations! You won the game!")
            break

# Example usage:
if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "grape", "mango"]
    play_game(word_list)





def play_game(word_list):
    """
    Function to run the Hangman game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost! The word was:", game.word)
            break
        elif game.num_letters > 0:
            game.get_user_input()
        else:
            print("Congratulations! You won the game!")
            break

# Call the play_game function to start the game
if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "grape", "mango"]
    play_game(word_list)


def validate_input(input_char):
    """Validates user input is a single alphabetical character."""
    if len(input_char) != 1 or not input_char.isalpha():
        print("Invalid input. Please enter a single alphabetical character.")
        return False
    return True

def process_guess(self, user_guess):
    """Process the guessed letter."""
    if user_guess in self.word:
        self.update_word_guessed(user_guess)
    else:
        self.reduce_lives(user_guess)

def update_word_guessed(self, letter):
    """Update the word guessed list with the correct letter."""
    self.word_guessed = [
        letter if char == letter else self.word_guessed[i]
        for i, char in enumerate(self.word)
    ]

def validate_and_append_guess(self, guess):
    """Validate and add a new guess."""
    if validate_input(guess):
        self.list_of_guesses.append(guess)


class Hangman:
    """
    A class to represent the Hangman game.

    Attributes:
        word (str): The word to be guessed.
        word_guessed (list): List of guessed letters with unguessed as '_'.
        num_lives (int): Remaining lives of the player.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initialize a Hangman game instance.

        Args:
            word_list (list): List of potential words for the game.
            num_lives (int): Number of lives the player starts with.
        """
        ...

def ask_for_input(self):
    """Prompt the user for input and process it."""
    while True:
        user_guess = input("Enter a letter: ").lower()
        if not validate_input(user_guess):
            continue
        if user_guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.list_of_guesses.append(user_guess)
            self.process_guess(user_guess)
            break
   

