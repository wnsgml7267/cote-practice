from collections import deque
n, k = map(int,input().split())
dx = set()
for i in range(n):
    dx.add(int(input()))
dx = list(dx)

graph = [0 for _ in range(k+1)] 

q = deque()
q.append(0)
graph[0] = 0
while q:
    x = q.popleft()
    if x == k:
        break
    for i in range(len(dx)):
        nx = dx[i] + x
        if 0 < nx <= k and graph[nx] == 0:
            graph[nx] = graph[x] + 1
            q.append(nx)
if graph[k] == 0:
    print(-1)
else:
    print(graph[k])

