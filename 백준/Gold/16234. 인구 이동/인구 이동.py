

from collections import deque
n, l, r = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))
#0 : 방문안함 or 국경선 닫힘, 1 : 방문 후 국경선 열림

q = deque()
qq = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = -1 #연합 유무
day = 0 #인구 이동 횟수
while cnt != 0:
  cnt = 0
  visited = [[0] * n for i in range(n)]
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0: #방문하지 않았으면 큐에 추가
        q.append((i,j))
        world_count = 0
        population = 0
        while q:
          x, y = q.popleft()
          for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
              t = abs(graph[x][y] - graph[nx][ny])
              if l <= t <= r:
                if visited[x][y] == 0:
                  world_count += 2
                  population += graph[nx][ny] + graph[x][y]
                  visited[x][y] = 1
                  visited[nx][ny] = 1
                  q.append((nx,ny))
                elif visited[x][y] == 1:
                  world_count += 1
                  population += graph[nx][ny]
                  visited[nx][ny] = 1
                  q.append((nx,ny))
        if world_count != 0:
          div = population//world_count
          qq.append((i,j))
          while qq:
            c, d = qq.popleft()
            for a in range(4):
              nx = c + dx[a]
              ny = d + dy[a]
              if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 1:
                if visited[x][y] == 1:
                  graph[x][y] = div
                  graph[nx][ny] = div
                  visited[x][y] = 2
                  visited[nx][ny] = 2
                  qq.append((nx,ny))
                elif visited[x][y] == 2:
                  graph[nx][ny] = div
                  visited[nx][ny] = 2
                  qq.append((nx,ny))
          cnt += 1
  day += 1
print(day-1)
