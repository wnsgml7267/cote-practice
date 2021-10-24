def multiplication(n):
  a = 1
  n = str(n)
  for i in n:
    a *= int(i)
  return a
print(multiplication(277777788888899))
