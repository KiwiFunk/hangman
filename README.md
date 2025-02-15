# Hangman
A simple CLI version of Hangman written in Python. Features a dictionary of word lists that can be called to give different themes of words to work from,
and enable more to be added in the future.

This is my first project in Python, so I wanted something simple that still touched on a lot of core features such as data storage types, logical operators, functions, string manipulation and loops. I made sure to eliminate the need for calling global variables by returning my data from my functions instead and unpacking it to variables when needed. Functions such as get_player_input expand on basic functions like input() to provide additional validation to prevent the user entering multiple characters or no characters - something not desirable in hangman. There are also optional parameters that can be used to make sure duplicate guesses cannot be made.

The game loop is pretty simple, with an ASCII title screen that waits for an input() before continuing into the outer loop. In the outer loop we assign get_wordlist() to a variable, which prompts the user to choose a set of words, then fetches it from wordsets.py using a key and returns its contents as a list. Lives, Round, and a list of incorrect guesses are also set here.

Our word to guess is then unpacked from a tuple provided by set_word, which randomly selects a word from the words list we previously created. This tuple contains both the target word to check against, and an obfuscated list containing underscores.

The game then enters its inner loop, where the player must guess letters. Each successful guess will result in an underscore from our obfuscated being replaced by the char, or the char being added to the incorrect guesses list. These are printed to the console each round by the update_game_display() function.

On game end, the user is then prompted to play again, returning to the lop of the outer loop, or exiting and clearing the console.