N = int(input())

def conq(n):
  if n == 1:
    return ['*']
  
  separate = conq(n//3)
  L = []
  for i in separate:
    L.append(i*3)
  for i in separate:
    L.append(i+' '*(n//3)+i)
  for i in separate:
    L.append(i*3)
  return L

print('\n'.join(conq(N)))
