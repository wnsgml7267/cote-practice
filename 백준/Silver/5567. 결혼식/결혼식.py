from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(m):
  x, y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

cnt = 0
q = deque()
visited[1] = True

for i in range(len(graph[1])):
  if not visited[graph[1][i]]:
    cnt += 1
    visited[graph[1][i]] = True
    q.append(graph[1][i])

while q:
  t = q.popleft()
  for i in range(len(graph[t])):
    if not visited[graph[t][i]]:
      cnt += 1
      visited[graph[t][i]] = True

print(cnt)


