# 1. Write a function that takes a list of integers as an argument, 
# and returns the sum of the integers. Use a try-except block to 
# catch any ValueError exceptions that may be raised when attempting to
#  convert a string to an integer.


def sum_integers(list):
  sum = 0 
# iterate over all integers in list and add each to max
# return an error in case of strings instead of integers in the list
  try:
    for num in list:
      sum += int(num)
    return sum
  except ValueError:
    return "An error occured while coverting string to integer"


  


print(sum_integers([1,3,4,5,]))
print(sum_integers(['q','b']))