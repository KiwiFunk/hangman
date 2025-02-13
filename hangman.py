import os
import random

#setup game variables
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon', 'xigua', 'yuzu', 'zucchini']
lives = 5

incorrect_guesses = []
round = 0

#create a function to chose a word, and display it as a series of underscores
def set_word():
    """
    Return a tuple containing the target word to guess, and an obfuscated list of equivalent length
    """
    obfuscated = []
    word = random.choice(words)
    for char in word:
        obfuscated.append('_')

    return word, obfuscated

def get_player_input(message):
    """
    Get input from player, make sure that it's only a single character, then return if valid
    """
    input_value = input(f'{message} \n')
    while len(input_value) != 1:
        input_value = input()
    return input_value
    

words = set_word()
target_word = words[0]
current_guess = words[1]

#Start Game Loop while player lives > 0
while lives > 0:
    os.system('cls')
    round += 1

    print(f'Current Round: {round} \n')
    print(f'{current_guess} \n')
    print(f"Incorrect Guesses: {', '.join(incorrect_guesses)}")
    print('\n')

    player_guess = get_player_input('Guess a Letter!')

    #Use containment operator to check if a letter is in the word. If it is, update the current guess with the letter, else, remove a life from the player and add guess to incorrect guesses list.
    if player_guess in target_word:
        #Using enumerate() to simplify indexing and iteration
        for i, char in enumerate(target_word):
            if char == player_guess:
                current_guess[i] = player_guess

    else:
        lives -= 1
        incorrect_guesses.append(player_guess)



    #create a function to update the word with the guessed letter. If every letter is guessed, break from loop

#end game console logs. You win/Game Over

#promt user to play again