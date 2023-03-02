# 2. Write a function to check if a given tuple is a palindrome, meaning the elements are the same in reverse order.

def tuple_is_palindrome(tup):
    return tup == tup[::-1]

# 1. Write a function to find the most common elements in a tuple.

def most_common(tup):
    return max(set(tup), key=tup.count)

    # Write a function to find all unique elements in a tuple and return them in a new tuple.

def unique(tup):
    return tuple(set(tup))

    # 4. Write a function that takes a tuple as an argument and returns a new tuple with only the even elements from the original tuple.


def even(tup):
    return tuple(i for i in tup if i % 2 == 0)

    # 5. Write a function that takes a tuple as an argument and returns a new tuple with only the odd elements from the original tuple.