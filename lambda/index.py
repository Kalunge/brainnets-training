#  Sort a list of dictionaries: Write a lambda function that sorts a list of dictionaries by a specified key. For example, given the list of dictionaries [{ 'name': 'John', 'age': 25 }, { 'name': 'Alice', 'age': 30 }, { 'name': 'Bob', 'age': 20 }], the lambda function should sort the list by age and return [{ 'name': 'Bob', 'age': 20 }, { 'name': 'John', 'age': 25 }, { 'name': 'Alice', 'age': 30 }].

def lambda_sort_dict_list(list, age):
    return sorted(list, key=lambda x: x[age])
   

sorted_list = lambda_sort_dict_list([{ 'name': 'John', 'age': 25 }, { 'name': 'Alice', 'age': 30 }, { 'name': 'Bob', 'age': 20 }], 'age')
print(sorted_list)

# Calculate the average: Write a lambda function that takes a list of numbers as input and returns the average value. For example, given the list [1, 2, 3, 4, 5], the lambda function should return 3.

def lambda_average(list):
    # use lambda
    return lambda list: sum(list) / len(list)

average = lambda_average([1, 2, 3, 4, 5])
print(average([1, 2, 3, 4, 5]))


# Find the largest number: Write a lambda function that takes a list of numbers as input and returns the largest number in the list. For example, given the list [1, 5, 3, 9, 2], the lambda function should return 9.


def lambda_largest(list):
    return lambda list: max(list)

largest = lambda_largest([1, 5, 3, 9, 2])
print(largest([1, 5, 3, 9, 2]))


# Flatten a nested list: Write a lambda function that takes a nested list as input and returns a flattened list. For example, given the nested list [1, [2, [3, 4], 5], 6], the lambda function should return [1, 2, 3, 4, 5, 6].

def lambda_flatten(list):
    return lambda list: [item for sublist in list for item in sublist]

flatten = lambda_flatten([1, [2, [3, 4], 5], 6])
print(flatten)
