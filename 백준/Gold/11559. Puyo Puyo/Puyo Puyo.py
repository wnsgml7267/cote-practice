from collections import deque

graph = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0

def bfs(a, b, color):
  q = deque()
  q.append((a,b))

  bomb = deque()
  bomb.append((a,b))

  visited = [[False] * 6 for _ in range(12)]
  visited[a][b] = True
  ball_cnt = 1 # 같은 구슬 색
  flag = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 12 and 0 <= ny < 6:
        if graph[nx][ny] == color and not visited[nx][ny]:
          q.append((nx,ny))
          bomb.append((nx,ny))
          visited[nx][ny] = True
          ball_cnt += 1
  if ball_cnt >= 4:
    flag = 1

    for x, y in bomb:
      graph[x][y] = '.'
  return flag

def down():
  for i in range(6):
    q = deque()
    for j in range(11, -1, -1):
      if graph[j][i] != '.':
        q.append(graph[j][i])
    for j in range(11, -1, -1):
      if q:
        graph[j][i] = q.popleft()
      else:
        graph[j][i] = '.'


for i in range(12):
  graph.append(list(input()))

while True:
  check = 0
  for i in range(12):
    for j in range(6):
      if graph[i][j] != '.':
        check += bfs(i,j,graph[i][j])
  if check == 0: # 터진 게 없으면
    print(cnt)
    break
  else:
    cnt += 1 # 연쇄적으로 터져도 1회 증가
  down()

