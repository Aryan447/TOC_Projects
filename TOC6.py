# Print out the fibonacci triangle

def fibonacci_triangle(n):
  """Prints the Fibonacci triangle of size n."""
  for i in range(n):
    row = []
    for j in range(i + 1):
      if j == 0 or j == i:
        row.append(1)
      else:
        row.append(row[j - 1] + row[j - 2])
    print(row)


if __name__ == "__main__":
  n = 10
  fibonacci_triangle(n)
