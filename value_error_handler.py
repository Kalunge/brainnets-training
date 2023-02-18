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


# 5. Write a function that takes a list of integers as an argument,
#  and returns the largest integer in the list. Use a try-except block to catch any ValueError exceptions that may be raised when
#  attempting to compare elements that are not integers.


def largest_int(list):
    max = 0
    for num in list:
        try:
            if num > max:
                max = num
        except ValueError:
            return "Only integers allowed"
        except TypeError:
          return "Integers cannot be compared to strings using > sign"

    return max


print(largest_int([1,2,4,77]))
print(largest_int([1,2,4,'77']))