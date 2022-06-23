from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
def direction(s,e):
  if s == e:
    return 0
  elif(s==1 and e==2) or (s==2 and e==1):
    return 2
  elif(s==3 and e==4) or (s==4 and e==3):
    return 2
  else:
    return 1
    
def bfs(start):
  q = deque()
  sx, sy, sd = start[0], start[1], start[2]
  #x, y, 방향, 명령횟수
  q.append((sx, sy, sd, 0))
  visited = set()
  while q:
    x,y,d,cnt = q.popleft()
    if x == end[0] and y == end[1]:
      return cnt + direction(d, end[2])
    #1~3칸
    for i in range(1,4):
      nx, ny = x + dx[d] * i, y + dy[d] * i
      #그래프 범위 (1,1)~(n,m) and 지나갈 수 있는 곳
      if 0 < nx <= n and 0 < ny <= m and graph[nx][ny] == 0:
        if (nx, ny, d, cnt + 1) not in visited:
          q.append((nx, ny, d, cnt + 1))
          visited.add((nx, ny, d, cnt+1))
      else:
        break
    for i in range(1, 5):
      if i != d and (x, y, i, cnt + 1) not in visited:
        q.append((x, y, i, cnt + direction(d, i)))
        visited.add((x, y, i, cnt + direction(d, i)))

#세로,가로
n, m = map(int,input().split())
#(1,1)~(n,m)
graph = [[0]*(m+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]
#출발점
start = list(map(int,input().split()))
#도착점
end = list(map(int,input().split()))

ans = bfs(start)
print(ans)
