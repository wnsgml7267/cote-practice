import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
q = deque()
visited[x] = 1
q.append(x)
answer = []
while q:
  x = q.popleft()
  for num in graph[x]:
    if not visited[num]:
      visited[num] = visited[x]+1
      if visited[num] == k+1:
        answer.append(num)
      q.append(num)
if len(answer) != 0:
  answer.sort()
  for i in answer:
    print(i)
else:
  print(-1)