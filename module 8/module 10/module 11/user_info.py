#!/usr/bin/env python
"""
Get a CSV file from the web and do some analysis on the data
"""
import sys
from urllib.request import urlopen
import csv


# TODO: Function to retrieve the file, create a dictionary with the data
def get_data(url):
    """Fetch data from a file from a URL

    Args:
        url (string): url address

    Returns:
        list: records
    """
    file_recs = []
    with urlopen(url) as url_file:
        for line in url_file:
            # decode binary data back to string
            # remove '\n' character
            # Save all the words to a list, and count the number of words
            line_recs = line.decode('utf-8').strip().split(',')
            file_recs.append(line_recs)
    return file_recs


def get_data_csv(data_file):
    data = []
    with open(data_file) as csv_file:
        csv_data = csv.DictReader(csv_file, delimiter=',')
        for row in csv_data:
            data.append(row) # add dictionaries to list
    return data


def all_state_recs(data):
    """Create a dictionary with a count of all state records

    Args:
        data (list of dictionaries): Data

    Returns:
        dict: state counts
    """
    # Create a list/set of all (unique) state values
    state_info = {}
    states = set()
    for val in data:
        for key in val:
            if key == 'state':
                states.add(val[key])
    for state in states:
        state_info[state] = state_recs(data, state)
    return state_info


def state_recs(data, state):
    total = 0
    for row in data:
        if row['state'] == state:
            total = total + 1
            print(row)
    return total


def analyze_data(data):
    # print records from 'UT' state
    # state_recs(data, state='UT')
    totals = all_state_recs(data)
    print(totals)


def main():
    """
    Main Driver
    """
    # url = 'http://icarus.cs.weber.edu/~hvalle/cs1400/MOCK_DATA.csv'
    # data = get_data(url)
    # print(data)
    data_file = 'MOCK_DATA.csv'
    data = get_data_csv(data_file)
    print(data)
    state_counts = all_state_recs(data)
    print(state_counts)
    analyze_data(data)


if __name__ == '__main__':
    main()
    sys.exit(0)