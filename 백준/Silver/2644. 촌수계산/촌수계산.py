n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            dfs(i)    
dfs(a)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b])

