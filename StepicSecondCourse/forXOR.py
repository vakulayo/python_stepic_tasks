
A = [5, 3, 2, 8, 9, 1, 6, 7, 10]
n = 10
def find_missing(A, n):
  result = 0

  for value in range(1, n + 1):
    result ^= value

  for value in A:
    result ^= value

  return result

print(find_missing(A, n))


