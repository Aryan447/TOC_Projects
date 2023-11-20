# Find the factorial of a number

def factorial(number):
  if number == 0:
    return 1
  else:
    return number * factorial(number - 1)


number = 3
factorial_of_number = factorial(number)
print("The factorial of {} is {}".format(number, factorial_of_number))
