
#MILESTONE 1
# import Library
import random

# Create a list containing the names of your 5 favorite fruits
word_list = ["Avocado", "Banana", "Mango", "Orange", "Grapes"]

# Print out the newly created list
print(word_list)

# Use the random.choice method and pass the word_list variable
randomWord = random.choice (word_list)

# print the random word
print(randomWord)

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
