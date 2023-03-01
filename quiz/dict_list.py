# 4. Write a function that takes a list of dictionaries as an argument, and returns the value of a
#  specified key from each dictionary. Use a try-except block to catch any KeyError exceptions that
#  may be raised when attempting to access a key that does not exist in a dictionary.


def access_values(dict_list, key):
  # iterate over the list of dictionaries
    for dict in dict_list:
      # try accessing the given key from the dictionary and print it
        try:
            print(dict[key])
      # handle keyError when key is not found
        except KeyError:
            print(f"the key {key} doest not exist in {dict}")


persons = [{"name": "Titus"}, {"names": "Muthomi"}, {"name": "Eric"}]
# persons

access_values(persons, "names")
