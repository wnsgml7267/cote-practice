import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
dx = (1,-1,0,0)
dy = (0,0,1,-1)
answer = []
q = deque()
def bfs():
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: 
          graph[i][j] = 0
          q.append((i,j))
          answer.append(bfs())
  
if len(answer) == 0:
  print(0)
  print(0)
else:
  print(len(answer))
  print(max(answer))