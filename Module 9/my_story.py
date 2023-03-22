#!/usr/bin/env python
"""
In this module we will use a Mad Libs game.
Mad Libs is a word game where players fill in the blanks
of a story with random words, resulting in humorous
tales.
"""
import sys

story = '''Once upon a time, there was a [adjective]  [animal]
        who lives in a [place]. this [animal] loved to [verb] and was
        always [adverb] [verb]-ing. One day, the [animal] met a [adjective]
        [person] who [verb]ed [adverb]ly. They decided to [verb] together
        and had a [adjective] time!'''

terms = {'adjective':'', 'animal':'', 'place':'',
         'verb':'', 'adverb':''}

def mad_libs(story):
    """This function takes a story and it will convert
    """
    words = story.split()
    # Access by elements
    #for word in words:
    #    print(word)
    terms= {}  # dictionary to save replacement
    # Access by index
    for index in range(len(words)):
        if '[' in words[index] and ']' in words[index]:
            # prompt = words[index].strip('[\]')
            prompt = words[index].replace('[', '')
            prompt = prompt.replace(']', '')
            if prompt not in terms:
                replacement = input(f'Enter a {prompt}')
                terms[prompt] = replacement
                words[index] = replacement
            else:
                words[index] = terms[prompt]

    new_story = ' '.join(words)
    return new_story


def main():
    """
    Main Driver
    """
    print(story)
    # Task: Create a function that prompts the user to enter words to fill in the blanks
    # of the story. This function should take the story as a string and return the completed story
    # as a string
    new_story = mad_libs(story)
    print(new_story)

if __name__ == '__main__':
    main()
    sys.exit(0)