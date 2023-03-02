# open test.text if exists

import os

def open_file():
    if os.path.exists("test.txt"):
        f = open("test.txt")
        print(f.read())
    else:
        print("File not found")

open_file()

# find patter in file mbox-short.txt and print the number of lines that match the pattern

# import re

# def find_pattern():
#     count = 0
#     with open("mbox-short.txt") as f:
#         for line in f:
#             if re.search("^From", line):
#                 count += 1
#     print(count)

# find_pattern()

# find patter of emails in file mbox-short.txt and print the number of lines that match the pattern

import re

def email_finder():
    count = 0
    with open("mbox-short.txt") as f:
        for line in f:
            if re.search("^From: ", line):
                count += 1
    print(count)

email_finder()

