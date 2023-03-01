# 2. Write a program that takes in a list of integers and returns the sum of all even numbers in the list.

def add_even(list):
  # create an empty list to append all even numbers
  even_numbers = []

  # loop through the given array and extract even numbers by checking if they are divisible by two using modullo
  for num in list:
    if num % 2 == 0:
      even_numbers.append(num)

# sum all even numbers in the array and return result
  return sum(even_numbers)



print(add_even([1,2,3,4,5,6, 10])
)