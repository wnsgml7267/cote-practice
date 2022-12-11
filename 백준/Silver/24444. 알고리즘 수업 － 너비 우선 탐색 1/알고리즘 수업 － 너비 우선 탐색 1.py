from collections import deque
n,m,l = map(int,input().split())

visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


q = deque()
visited[l] = 1
q.append(l)
cnt = 2
while q:
    
    x = q.popleft()
    graph[x].sort()
    for i in graph[x]:
        if not visited[i]:
            visited[i] = cnt
            cnt += 1
            q.append(i)
            
for i in range(1,n+1):
    print(visited[i])
