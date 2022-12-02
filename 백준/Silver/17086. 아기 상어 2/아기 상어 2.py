from collections import deque
n, m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))

dx = (0,0,1,-1,1,-1,1,-1)
dy = (1,-1,0,0,1,-1,-1,1)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      visited = [[False] * m for _ in range(n)]
      visited[i][j] = True
      q = deque()
      q.append((i,j))
      while q:
        x, y = q.popleft()
        
        for k in range(8):
          nx = dx[k] + x
          ny = dy[k] + y
          if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1 and not visited[nx][ny]:
            if (graph[nx][ny] != 0 and graph[x][y] + 1 < graph[nx][ny]) or graph[nx][ny] == 0:
              visited[nx][ny] = True
              graph[nx][ny] = graph[x][y] + 1
              q.append((nx,ny))
print(max(map(max, graph))-1)


