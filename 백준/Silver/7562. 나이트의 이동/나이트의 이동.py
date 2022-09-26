import sys
input = sys.stdin.readline
from collections import deque
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]
for i in range(int(input())):
  n = int(input()) #한 변의 길이
  now_x, now_y = map(int,input().split()) #현재 좌표
  end_x, end_y = map(int,input().split()) #도달할 좌표
  graph = [[0]*n for i in range(n)]
  q = deque()
  q.append((now_x, now_y))
  while q:
    x, y = q.popleft()
    if x == end_x and y == end_y:
      break
    for j in range(8):
      nx = x + dx[j]
      ny = y + dy[j]
      if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx,ny))
  print(graph[end_x][end_y])