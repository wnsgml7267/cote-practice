import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
graph = []
answer = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = (1,-1,0,0), (0,0,1,-1)
  
for i in range(n):
  graph.append(list(map(int,input().split())))
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0 or graph[i][j] == 2:
      answer[i][j] = 0
      visited[i][j] = True
      if graph[i][j] == 2:
        q = deque()
        q.append((i,j))
      
while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = dx[i] + x, dy[i] + y
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
      visited[nx][ny] = True
      answer[nx][ny] = answer[x][y] + 1
      q.append((nx,ny))
for i in range(n):
  print(*answer[i])