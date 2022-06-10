from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
#가로, 세로
M, N = map(int,input().split())
graph = []
#벽 부순 횟수
broken_count = [[-1]*M for _ in range(N)]

for _ in range(N):
  graph.append(input())
  
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()
q.append((0,0))
broken_count[0][0] = 0
while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M:
      #벽 부순 횟수를 체크 안한 곳
      if broken_count[nx][ny] == -1:
        #벽이 없는 방
        if graph[nx][ny] == '0':
          #이전에 있던 방 부순 횟수와 동일
          broken_count[nx][ny] = broken_count[x][y]
          #방 부순 횟수가 적은 경로를 우선 탐색하기위해 appendleft
          q.appendleft((nx,ny))
        #벽이 있는 방
        else:
          #방 부순 횟수 +1          
          broken_count[nx][ny] = broken_count[x][y] + 1
          q.append((nx,ny))

print(broken_count[N-1][M-1])

  
  