from collections import deque
n = int(input())
graph = []
q = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []
for i in range(n):
  graph.append(list(map(int,input().split())))
mx = max(map(max, graph))
for i in range(1, mx+1):
  visited = [[False]*n for _ in range(n)]
  cnt = 0
  for j in range(n):
    for k in range(n):
      if visited[j][k] == False and graph[j][k] >= i:
        q.append((j,k))
        visited[j][k] = True
        cnt += 1
      while q:
        x, y = q.popleft()
        for l in range(4):
          nx = x + dx[l]
          ny = y + dy[l]
          if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] >= i:
            visited[nx][ny] = True
            q.append((nx,ny))
  answer.append(cnt)
print(max(answer))