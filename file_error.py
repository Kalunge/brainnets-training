# 2. Write a function that takes a filename as an argument, and attempts to
#  open the file. Use a try-except block to catch any FileNotFoundError
#   exceptions that may be raised when attempting to open the file. If the file is successfully opened,
#  the function should return the contents of the file.

def read_file(file_name):
  try:
    file_details = open(file_name)
    print(file.read(file_details))
  except FileNotFoundError:
    print("File not found")

read_file('hello.txt')