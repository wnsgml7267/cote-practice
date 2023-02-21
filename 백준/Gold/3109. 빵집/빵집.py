'''
 탐색은 맨 밑 행부터 시작한다.
 탐색 방향 순서가 필요하다.
 1. 대각선 아래
 2. 직선
 3. 대각선 위
 BFS를 돌린다.
 빵집에 도착하면 멈춘다.
'''
from collections import deque

n, m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(input()))
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0 # 파이프라인 최대 개수
dx , dy = (1,0,-1), (1,1,1)
def bfs(a,b):
  global cnt

  if b == m-1:
    cnt += 1
    return True
  visited[a][b] = True
  
  for i in range(3):
    nx, ny = dx[i] + a, dy[i] + b
    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == ".":
      # 빵집에 도착했다면 파이프라인 증가!
      if(bfs(nx, ny)): return True
        
  return False

# 맨 밑 행부터 탐색 시작
for i in range(n-1, -1, -1):
  bfs(i,0)

print(cnt)

# print(visited)