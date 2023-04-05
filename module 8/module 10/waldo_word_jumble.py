"""
The waldo word jumble game, will present the user with a 'jumble' word
The user must identify the correct word, based on the difficulty (input parameter)
The system will keep track of correct and incorrect tries
The game stays on until th euser decides to quit.
"""
import sys
import random

# Define a list of words
words = 'Python computer programming language is one of the best thing I have ever learned, it has many functions and uses to benefit from'

def word_jumble(difficulty):
    """Select the word difficulty based on the input
    if word < 5, then, easy
    elif word < 8, then, medium
    else hard
    Args:
        difficulty (string): difficulty level
    """
    # TODO: Set difficulty level
    input('for easy enter 1', 'for medium enter 2', 'for hard enter 3')
    # TODO: Create a loop that will ask user if he wants to continue
    if difficulty == "1":
        word_list = [word for word in words if len(word) < 5]
    elif difficulty == "2":
        word_list = [word for word in words if len(word) < 8  and len(word) >= 5]
    else:
        word_list = [word for word in words if len(word) >= 8]
    play_again = True
    score = 0
    while play_again:
        # TODO: Select a random word from the list
        x = random.choice(word_list)
        # TODO: 'Jumble' the selected word
        jumbled_word = ''
        print("Guess the original word:", jumbled_word)
        guess = input().strip().lower()
        # TODO: Present choice to user, and compare input
        guess = input(f'Unscramble the word: {jumble_word}\n')
        if guess.lower( == word:)
        
def main(name, age):
    """
    Main Driver
    """
    print(words)

if __name__ == '__main__':
    # TODO: Check input parameters
    # TODO: print help messages
    # main()
    # TODO: If good to go, call word
    sys.exit()
