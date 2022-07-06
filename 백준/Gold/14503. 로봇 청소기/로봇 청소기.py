import sys
input = sys.stdin.readline
n,m = map(int,input().split()) #세로,가로
r,c,d = map(int,input().split()) #청소기 좌표, 방향
graph = [list(map(int,input().split())) for i in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1,0,1,0] #북,동,남,서 => 0 1 2 3
dy = [0,1,0,-1]
visited[r][c] = 1
count = 1 #청소 횟수

while 1:
  flag = 0
  for _ in range(4):
    nx = r+dx[(d+3)%4] #0321 왼쪽방향 순서
    ny = c+dy[(d+3)%4]  

    d = (d+3)%4

    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
      if visited[nx][ny] == 0:
        visited[nx][ny] = 1
        count += 1
        r = nx
        c = ny
        flag = 1
        break
  if flag == 0:
    if graph[r-dx[d]][c-dy[d]] == 1:
      print(count)
      break
    else:
      r,c = r-dx[d],c-dy[d]

