# swap two numbers with a third variable

def swap_numbers(a, b):
  temp = a
  a = b
  b = temp
  return a, b


a = 10
b = 20

print("Before swapping:")
print("a = ", a)
print("b = ", b)

a, b = swap_numbers(a, b)

print("After swapping:")
print("a = ", a)
print("b = ", b)
