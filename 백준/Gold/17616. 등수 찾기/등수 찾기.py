from collections import deque

n, m, x = map(int,input().split())

up = [[] for _ in range(n+1)] # 등수 높은 학생들 담기
down = [[] for _ in range(n+1)] # 등수 낮은 학생들 담기
visited = [False] * (n+1)

def bfs(s, graph):
    q = deque()
    q.append(s)
    visited[s] = True
    cnt = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt
                

for i in range(m):
    a, b = map(int,input().split())
    up[b].append(a)
    down[a].append(b)

print(1+bfs(x,up), n-bfs(x,down))