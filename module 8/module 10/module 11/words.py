"""
Count the number of words from file located at web server
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a file from a URL

    Args:
        url (string): url address

    Returns:
        list words
    """
    file_words = []
    with urlopen(url) as url_file:
        for line in url_file:
            # decode binary data back to string
            line_words = line.decode('utf-8').strip().split
            for word in line_words:
                file_words.append(word)
    return file_words

def main():
    """
    Main Driver
    """
    url = 'http://icarus.cs.weber.edu/~hvalle/cs1400/MOCK_DATA.csu'
    # Open web file
    poem_words = fetch_words(url)
    total_words = len(poem_words)
    print(f'You have a total of {total_words} in the file')
    for word in poem_words:
        if word[0] == 'p' or word[-1] == 'y':
            print(word)


if __name__ == '__main__':
    main()
    sys.exit()