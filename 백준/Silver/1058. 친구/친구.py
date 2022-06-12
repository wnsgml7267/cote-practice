n = int(input())
f = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  for j in range(n):
    for k in range(n):
      if j == k :
        continue
      if f[j][k]=='Y' or (f[j][i]=='Y' and f[i][k]=='Y'):
        visited[j][k]=1
result = 0
for i in visited:
  result = max(result, sum(i))
print(result)