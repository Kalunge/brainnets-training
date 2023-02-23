def find_largest(numbers):
    largest = None
    for number in numbers:
        if largest is None or number > largest:
            largest = number
    return largest

    



numbers = [-1,-2,-3,-4]
numbers = [-1,-2,-3,-4, 44]
print(find_largest(numbers))

def find_duplicates(arr):
    #return list of duplicates just once in the list

    result = []
    for i in range(len(arr)):
        if arr[i] in arr[i+1:] and arr[i] not in result:
            result.append(arr[i])
    return result
    

input_arr = [1, 2, 3, 4, 2, 3, 5, 6, 7, 3]
output = find_duplicates(input_arr)
print(output)


def divide(x, y):
    if x == 0 or y == 0:
      return None
    else:
        return x/y


result1 = divide(8, 2)
print(result1)


def print_data():
  data = ["item1", "item2", "item3"]
  for i in range(len(data)):
    print(data[i])

print_data()    