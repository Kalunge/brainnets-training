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



    # 2. Write a Python program that reads a CSV file and converts it into a dictionary. Each row of the CSV file should be a key-value pair in the dictionary.

import csv

def csv_to_dict(filename):
    """Convert a CSV file to a dictionary."""
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        my_dict = dict(reader)
    return my_dict




    # 3. Write a Python program that reads a binary file and converts it into a hexadecimal string. The program should output the hexadecimal string to a text file.

def bin_to_hex(filename):
    """Convert a binary file to a hexadecimal string."""
    with open(filename, 'rb') as f:
        data = f.read()
        hex_data = data.hex()
    return hex_data




# 4. Write a Python program that reads a text file containing numbers and calculates the sum of all the numbers in the file.

def sum_numbers(filename):
    """Calculate the sum of all the numbers in a file."""
    with open(filename, 'r') as f:
        numbers = f.readlines()
        numbers = [int(x.strip()) for x in numbers]
        total = sum(numbers)
    return total


# 5. Write a Python program that reads a text file and removes all the blank lines. The modified text should be written back to the file.

def remove_blank_lines(filename):
    """Remove all the blank lines from a file."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines if x.strip()]
    return lines




