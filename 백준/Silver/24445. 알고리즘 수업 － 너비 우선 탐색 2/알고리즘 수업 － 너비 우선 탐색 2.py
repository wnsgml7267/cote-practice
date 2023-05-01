import sys
input = sys.stdin.readline
from collections import deque
n, m, k = map(int,input().split()) 
arr = []
graph = [[ ] for _ in range(n+1)]
q = deque()
visited = [0] * (n+1)
visited[k] = 1
cnt = 1
q.append(-k)
for i in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
for i in graph:
  i.sort(reverse=True)
while q:
  x = -q.popleft()
  for i in graph[x]:
    if not visited[i]:
      q.append(-i)
      cnt += 1
      visited[i] = cnt
for i in visited[1:]:
  print(i)