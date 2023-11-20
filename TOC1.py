# find the maximum number in an array of integer

def find_max(array):
  max_number = array[0]
  for number in array:
    if number > max_number:
      max_number = number
  return max_number


array = [10, 4, 2, 9, 7, 5, 1, 3, 6, 8]
max_number = find_max(array)
print(max_number)