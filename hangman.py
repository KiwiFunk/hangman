#import packages
import os
import random

#setup game variables
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon', 'xigua', 'yuzu', 'zucchini']
lives = 5

word_to_guess = ''
current_guess = ''
incorrect_guesses = []
round = 0

#create a function to chose a word, and display it as a series of underscores
def set_word():
    global word_to_guess
    global current_word

    word_to_guess = random.choice(words)
    for char in word_to_guess:
        current_guess.append('_')
    

#Start Game Loop while player lives > 0

#create a function to check if a letter is in the word. If it is, update the word with the letter, else, remove a life from the player

#create a function to update the word with the guessed letter. If every letter is guessed, break from loop

#end game console logs. You win/Game Over

#promt user to play again