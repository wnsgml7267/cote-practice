from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

q = deque()
n = int(input()) #보드의 크기n x n
apple_count = int(input()) #사과의 개수
board = [[0]*(n+1) for i in range(n+1)] #보드 (n+1)x(n+1) , 1행1열부터 시작이니까
visited = [[0]*(n+1) for i in range(n+1)]
for i in range(apple_count):
  ax, ay = map(int,input().split())
  board[ax][ay] = 1 # 사과 위치 표시 1
l = int(input()) #뱀의 방향 변환 횟수
second = [] #몇 초 뒤
direction = [] #방향 L,D 왼쪽,오른쪽 90도
d = 0
for i in range(l):
  s,c = input().split() #몇초 뒤 , 방향 변환
  second.append(int(s))
  direction.append(c)
dx = [0,-1,0,1] #동,북,서,남 (왼쪽)
dy = [1,0,-1,0] #0  1  2  3
count = 0
def snake(x,y,visited,d):
  global count #몇초 뒤 끝나는지
  visited[x][y]=1 #방문체크
  q.append([x,y])
  nx = x + dx[d]
  ny = y + dy[d]
  if 0 < nx <= n and 0 < ny <= n and visited[nx][ny] == 0: #방문하지 않았다
    for i in range(len(second)):
      if second[i] == count+1: #방향 전환 할 시간
        if direction[i] == "L": #왼쪽
          d += 1
          if d == 4:
            d = 0
        elif direction[i] == "D": #오른쪽
          d -= 1
          if d == -1:
            d = 3
    if board[nx][ny] == 1: #사과가 있으면 꼬리 늘어남
      board[nx][ny] = 0 #사과 없앰
      count += 1 #1초 늘려줌
      snake(nx,ny,visited,d)
    else: #없으면 안늘어남
      a,b = q.popleft()
      visited[a][b] = 0 #뱀 이동
      count += 1 #1초 늘려줌
      snake(nx,ny,visited,d)
    
  else: #벽에 닿이거나 몸에 닿이면
    count += 1
    print(count)
    return
    
snake(1,1,visited,d) #x,y좌표,방문체크(뱀의 위치),방향(0 동쪽부터)