# 3. Write a function that takes a list of strings as an argument,
#  and returns a new list containing only the strings that can be
#  successfully converted to a float. Use a try-except block to catch any ValueError exceptions that may be
# raised when attempting to convert a string to a float.


def convert_to_float(list):
  # create a list to hold strings that can be converted to floats
    convertable_strs = []

    # iterate over the array of strings and try to convert them into a float
    # if convertable they will be added to the arry else deal with value error exception accordingly
    for str in list:
        try:
            float(str)
            convertable_strs.append(str)

        except:
            return f"{str} cannot be converted to a float"

    return convertable_strs


print(convert_to_float(["1", "2", "3"]))
print(convert_to_float(["1", "2", "3", "c"]))
