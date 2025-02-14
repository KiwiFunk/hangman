"""
A collection of lists containing themed words to load into the hangman game.
"""

def return_wordlist(set):
    """
    Return a specified list of words
    """
    requested_list = wordsets[set]
    return requested_list

wordsets = {
    1: [
        'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 
        'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon', 'xigua', 'yuzu', 'zucchini'
    ],
    2: [
        'argentina', 'brazil', 'canada', 'denmark', 'egypt', 'france', 'germany', 'hungary', 'ireland', 'italy', 'japan',
        'kenya', 'luxembourg', 'mexico', 'netherlands', 'taiwan', 'portugal', 'qatar', 'russia', 'spain', 'turkey',
        'ukraine', 'vietnam', 'yemen', 'zimbabwe', 'australia', 'belgium', 'chile', 'czechia', 'ethiopia',
        'finland', 'greece', 'iceland', 'jamaica', 'kazakhstan', 'lebanon', 'malaysia', 'norway', 'poland', 'scotland', 'sweden'
    ],
    3: [
        'alligator', 'antelope', 'baboon', 'bear', 'bison', 'binturong', 'camel', 'cheetah', 'chimpanzee', 'crocodile', 'deer', 'elephant', 
        'flamingo', 'fox', 'giraffe', 'gorilla', 'hippopotamus', 'hyena', 'kangaroo', 'koala', 'leopard', 'lion', 'meerkat', 
        'monkey', 'ostrich', 'otter', 'panda', 'parrot', 'penguin', 'rhinoceros', 'seal', 'sloth', 'snake', 'tiger', 'tortoise', 
        'vulture', 'walrus', 'wolf', 'wombat', 'zebra', 'porcupine', 'armadillo', 'lemur', 'wallaby', 'anteater'
    ]
}