#.지나갈 수 있는 공간
#J지훈이 위치
#F불 위치
from collections import deque
r, c = map(int,input().split())
graph = []
for i in range(r):
  graph.append(list(input()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

minsu_visited = [[0] * c for i in range(r)] #방문한 시간
fire_visited = [[0] * c for i in range(r)] #방문한 시간

minsu = deque() #민수 좌표
fire = deque() #불 좌표

for i in range(r):
  for j in range(c):
    if graph[i][j] == "J":
      minsu.append((i,j))
      minsu_visited[i][j] = 1 #0분부터 시작인데 결국 탈출할 시 1분을 더해줘야 하기 때문.
    elif graph[i][j] == "F":
      fire.append((i,j))
      fire_visited[i][j] = 1

def bfs():
  while fire:
    x, y = fire.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c:
        if not fire_visited[nx][ny] and graph[nx][ny] != "#":
          fire_visited[nx][ny] = fire_visited[x][y] + 1
          fire.append((nx,ny))
  while minsu:
    x, y = minsu.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c:
        if not minsu_visited[nx][ny] and graph[nx][ny] != "#":
          if not fire_visited[nx][ny] or fire_visited[nx][ny] > minsu_visited[x][y] + 1:
            minsu_visited[nx][ny] = minsu_visited[x][y] + 1
            minsu.append((nx, ny))
      else: #탈출 시
        return minsu_visited[x][y]
  return "IMPOSSIBLE" #미탈출
print(bfs())


