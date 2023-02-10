import sys
input = sys.stdin.readline
from collections import deque
a, b = map(int,input().split())
n, m = map(int,input().split())

'''
1~n의 문자
m개의 문자 쌍
'''
# 양방향 
graph = [[] for _ in range(n+1)]

for i in range(m):
  x, y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

mn = 10**9


visited = [0] * (n+1)
visited[a] = 1
cnt = 0

q = deque()
q.append(a)
while q:
  x = q.popleft()

  if x == b:
    mn = min(mn, visited[x]-1)
    break

  for j in range(len(graph[x])):
    if not visited[graph[x][j]]:
      visited[graph[x][j]] = visited[x] + 1
      q.append(graph[x][j])
if mn == 10**9:
  print(-1)
else:
  print(mn)