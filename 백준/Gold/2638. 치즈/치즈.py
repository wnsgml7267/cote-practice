from collections import deque
n, m = map(int,input().split())
graph = []
dx, dy = (1,-1,0,0), (0,0,1,-1)
# 치즈 1, 공기 0
for i in range(n):
  graph.append(list(map(int,input().split())))
time = 0

def check(): # 치즈가 있으면 True, 없으면 False
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        return True
  return False
def out(): # 외부 벽 체크

  q = deque()
  q.append((0,0))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = dx[i] + x , dy[i] + y
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        q.append((nx,ny))
def melt(): # 녹일 수 있는 치즈 녹이기
  # 치즈 좌표 큐에 넣기
  c_q = deque()
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        c_q.append((i,j))
  
  while c_q:
    x, y = c_q.popleft()
    cnt = 0
    for j in range(4):
      nx, ny = dx[j] + x , dy[j] + y
      if graph[nx][ny] == 0 and visited[nx][ny] == 1: # 공기이자 외부 벽인 경우
        cnt += 1
    if cnt >= 2: # 외부 벽이 2개 이상인 경우 녹는다.
      graph[x][y] = 0
      
  
while True:
  if check(): # 치즈가 모두 녹을 때까지

    time += 1
    # 0. 방문 초기화
    visited = [[0 for _ in range(m)] for _ in range(n)] 
    # 1. 외부 벽 체크 (외부 벽을 1로 만듦)
    out()
    
    # 2. 치즈 녹이기
    melt()
    
  else:
    break
  
print(time)