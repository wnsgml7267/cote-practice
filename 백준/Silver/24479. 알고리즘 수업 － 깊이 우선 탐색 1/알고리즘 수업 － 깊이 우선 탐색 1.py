import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, l = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 1

def dfs(x):
    global cnt
    visited[x] = cnt
    graph[x].sort()
    for i in graph[x]:
        if not visited[i]:
            cnt += 1
            dfs(i)
dfs(l)

for i in range(1,n+1):
    print(visited[i])

