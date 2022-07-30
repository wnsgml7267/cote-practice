n,m=map(int,input().split())
array = []
for i in range(n*2):
  array.append(list(map(int,input().split())))
answer = [[0] * m for i in range(n)]
for i in range(n):
  for j in range(m):
    answer[i][j] = array[i][j]+array[i+n][j]
for i in range(n):
  print(*answer[i])