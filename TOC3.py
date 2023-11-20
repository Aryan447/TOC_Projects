# write a program to find the reverse of a number

def reverse_number(number):
  reversed_number = 0
  while number > 0:
    remainder = number % 10
    reversed_number = reversed_number * 10 + remainder
    number //= 10
  return reversed_number


number = 1234
reversed_number = reverse_number(number)
print("The reverse of {} is {}".format(number, reversed_number))
