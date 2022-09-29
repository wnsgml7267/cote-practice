from collections import deque
#적록색약 : RG 묶어서
n = int(input())
graph = []
for i in range(n):
  graph.append(list(input()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
  q.append((a,b))
  visited[a][b] = True

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        if graph[x][y] == graph[nx][ny]:
          q.append((nx, ny))
          visited[nx][ny] = True

q=deque()
visited = [[False]*n for i in range(n)]
common_count = 0   
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      common_count += 1

q=deque()
visited = [[False]*n for i in range(n)]
special_count = 0
for i in range(n):
  for j in range(n):
    if graph[i][j] == "R":
      graph[i][j] = "G"
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      special_count += 1
print(common_count, special_count)