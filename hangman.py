import os
import random
import time
from wordsets import return_wordlist

#setup game variables
game_running = True

def get_wordlist():
    """
    Prompts the user to select a set of words, then returns the selected set as a list.
    """
    #Add any new sets of words to this string. Make sure to use the correct number/key
    options = "1) Fruits\n2) Countries\n3) Animals\n4) Food\n5) English words"

    print(f"Welcome to hangman! Please select a set of words to play from!\n{options}")

    while True:
        user_input = get_player_input("Enter the number for the set you want to play!")
        if user_input.isdigit() and f"{user_input})" in options:
            break
        else:
            print("Invalid input. Please enter a valid number from the options above.")
    return return_wordlist(int(user_input))

def set_word():
    """
    Return a tuple containing the target word to guess, and an obfuscated list of equivalent length
    """
    obfuscated = []
    word = random.choice(words)
    for char in word:
        if char == ' ':
            obfuscated.append(char)
        else:
            obfuscated.append('_')

    return word, obfuscated

def get_player_input(message):
    """
    Get input from player, make sure that it's only a single character, then return when valid

    Parameters:
    message (string): Text to display in the input prompt.

    Returns:
    string value
    """
    input_value = input(f'{message} \n')
    while len(input_value) != 1:
        input_value = input()
    return input_value

def update_game_display(current_round, current_lives, current_guess_word, current_incorrect_guesses):
    """
    Update the console with the current game status. 
    Take variables as parameters to make sure we dont rely on variables that may not exist yet.

    Parameters:
    current_round (int): Current round number of this game.
    current_lives(int): Remaining player lives.
    current_guess_word (list): The current state of the word being guessed.
    current_incorrect_guesses (list): A list of any incorrect guesses thus far.

    Returns:
    None
    """
    os.system('cls')

    print(f'Current Round: {current_round}\tLives: {current_lives}\n')
    print(f'{current_guess_word} \n')
    print(f"Incorrect Guesses: {', '.join(current_incorrect_guesses)}")
    print('\n')
    
#Outer Game loop to handle each game
while game_running:

    os.system('cls')

    #Prompt user to select a set of words to play from
    words = get_wordlist()

    #Reset variables for new round
    lives = 5
    round = 0
    incorrect_guesses = []

    #Unpack tuple return from set_word
    target_word, current_guess = set_word()

    #Inner game loop to handle rounds of current game
    while lives > 0:
        
        round += 1

        update_game_display(round, lives, current_guess, incorrect_guesses)

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
            update_game_display(round, lives, current_guess, incorrect_guesses)
            time.sleep(0.7)
            break;

    #End Game Scenarios

    os.system('cls')
    
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