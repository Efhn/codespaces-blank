#!/usr/bin/env python
"""
In this module we will use a Mad Libs game.
Mad Libs is a word game where players fill in the blanks
of a story with random words, resulting in humorous
tales.
"""
import sys

story = '''Once upon a time, there was a [adjective] [animal]
who lived in a [place]. This [animal] loved to [verb] and was 
always [adverb] [verb]-ing. One day, the [animal] met a [adjective]
[person] who [verb]ed [adverb]ly. They decided to [verb] together
and had [adjective] time!'''
        '''Once upon a time, there was a white rabbit
        who lived in a hole. this rabbit loved to play and was
        always happily playing. One day, the rabbit met a small
        kid who played frequently.

def mad_libs(story):
    new_story = ''
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