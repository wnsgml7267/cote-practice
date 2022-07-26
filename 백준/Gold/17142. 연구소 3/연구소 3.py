from collections import deque
from itertools import combinations as cb
n,m=map(int,input().split()) #연구소 크기, 활성 바이러스
graph = [list(map(int,input().split())) for i in range(n)]
active_virus=[] #활성 바이러스들
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 10**9
def bfs(virus):
  global ans
  spread = [[-1]*n for i in range(n)]
  q=deque()
  for i in virus:
    q.append(i)
    spread[i[0]][i[1]] = 0 #첫 활성된 바이러스는 0 표시
  max_sp = 0
  while q:
    x,y =q.popleft()
    for j in range(4):
      nx = x+dx[j]
      ny = y+dy[j]
      if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 1 and spread[nx][ny] == -1:
        spread[nx][ny] = spread[x][y]+1 #시간 초 증가
        if graph[nx][ny] == 0:
          max_sp = max(max_sp, spread[nx][ny]) #걸린 시간
        q.append([nx,ny]) 
  a=list(sum(spread,[]))
  if a.count(-1)==list(sum(graph,[])).count(1): #벽에 개수가 같으면 바이러스가 다 퍼진 것.
    ans = min(ans,max_sp)    
    
for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      active_virus.append([i,j])
for ac_vr in cb(active_virus, m): #m개의 활성 바이러스 좌표 리스트
  bfs(ac_vr)
if ans == 10**9:
  print(-1)
else:
  print(ans)




