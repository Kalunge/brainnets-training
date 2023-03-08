    # 1. Write a Python program that reads a text file and prints the number of lines, words, and characters in the file.

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)

    # 2. Write a Python program that reads a CSV file and converts it into a dictionary. Each row of the CSV file should be a key-value pair in the dictionary.

import csv

def csv_to_dict(filename):
    """Convert a CSV file to a dictionary."""
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        my_dict = dict(reader)
    return my_dict

filename = 'data.csv'
my_dict = csv_to_dict(filename)


    # 3. Write a Python program that reads a binary file and converts it into a hexadecimal string. The program should output the hexadecimal string to a text file.
    # 4. Write a Python program that reads a text file containing numbers and calculates the sum of all the numbers in the file.
    # 5. Write a Python program that reads a text file and removes all the blank lines. The modified text should be written back to the file.

