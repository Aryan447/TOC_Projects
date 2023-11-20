# Find greatest common divisior of two number

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a


a = 10
b = 20
gcd_of_numbers = gcd(a, b)
print("The greatest common divisor of {} and {} is {}".format(a, b, gcd_of_numbers))
