n, m = map(int,input().split())
array = []
def back(num):
  if len(array) == m: #다 골랐으면
    print(' '.join(map(str, array)))
    return
  for i in range(num, n+1):
    array.append(i)
    back(i)
    array.pop()
back(1)