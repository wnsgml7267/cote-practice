import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
cnt = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
  array = list(map(int,input().split()))
  bb = []
  for i in range(0, len(array), 3):
    bb.append(sum(array[i:i+3])//3)
  graph.append(bb)
t = int(input())
visited = [[False]*m for i in range(n)]

def bfs(x,y):
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if visited[nx][ny] == False and graph[nx][ny] >= t:
        bfs(nx,ny)
for i in range(n):
  for j in range(m):
    if visited[i][j] == False and graph[i][j] >= t:
      bfs(i,j)
      cnt += 1
print(cnt)
  