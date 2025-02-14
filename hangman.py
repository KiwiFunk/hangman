import os
import random

#setup game variables
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon', 'xigua', 'yuzu', 'zucchini']

incorrect_guesses = []
game_running = True

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
    Get input from player, make sure that it's only a single character, then return when valid
    """
    input_value = input(f'{message} \n')
    while len(input_value) != 1:
        input_value = input()
    return input_value
    
#OUTER LOOP FOR GAME REPEAT HERE
while game_running:
    #Set lives and counter for new round
    lives = 5
    round = 0
    #Unpack tuple return from set_word
    target_word, current_guess = set_word()

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

        #If every letter is correctly guessed, break from loop
        if '_' not in current_guess:
            break;

    #End Game Scenarios
    if lives > 0:
        print("Congrats, you win!")
    else:
        print("You lose :c")

    #prompt user to play again
    play_again = get_player_input("Do you want to play again? (y/n)")
    while play_again not in ('y', 'n'):
        play_again = get_player_input("Please enter y or n")
    if play_again == 'n':
        game_running = False