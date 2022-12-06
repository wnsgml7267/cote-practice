from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().split())

answer = []
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

q = deque()
q.append(x)
visited[x] = 0

while q:
    x = q.popleft()
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            q.append(i)

for i in range(1,n+1):
    if visited[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)