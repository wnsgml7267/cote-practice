import sys
from collections import deque
#x, y 경우의 수 저장(중복 방지)
def pour(x, y):
  if not visited[x][y]:
    visited[x][y] = True
    q.append((x,y))
def bfs():
  while q:
    x, y = q.popleft() #x : a물통 물의 양, y : b물통 물의 양
    z = c - x - y #c물통에 들어있는 물의 양

    if x == 0: #a물통이 비어 있으면 c물통에 남아있는 양 저장
      answer.append(z)
    water = min(x, b-y) # x=>y로 옮길 물. x전체를 옮기거나 b물통을 꽉채움
    pour(x - water, y + water) #옮긴 후의 x와 y의 상태를 큐에 저장
    water = min(x, c-z)
    pour(x - water, y)
    water = min(y, a-x)
    pour(x + water, y - water)
    water = min(y, c-z)
    pour(x, y - water)
    water = min(z, a-x)
    pour(x + water, y)
    water = min(z, b-y)
    pour(x, y + water)
    
a,b,c=map(int,input().split())
q=deque()
q.append((0,0))

visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True

answer = []

bfs()

answer.sort()
print(*answer)