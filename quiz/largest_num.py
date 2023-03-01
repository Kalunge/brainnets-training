# 4. Write a program that takes in a list of integers and returns the largest number in the list that is also divisible by 3.
def larges_divesible_by_3(arr):
  max = 0

  # loop through the given list and find a number greater than maximum and is divisble by
  #  three then overite max with the number
  for num in arr:
    if num % 3 == 0 and num % 3 == 0:
     max = num

  return max


print(larges_divesible_by_3([1,4,7,9,4,77]))
print(larges_divesible_by_3([1,4,7,9,4,77, 99, 100]))
print(larges_divesible_by_3([1,4,7,9,4,77, 99, 100, 120, 121]))
print(larges_divesible_by_3([1,4,7,9,4,77, 99, 100, 120, 121, 123]))