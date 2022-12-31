from collections import deque

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
dx = (0,0,-1,1,1,1,-1,-1)
dy = (1,-1,0,0,-1,1,1,-1)
cnt = 0

def bfs(i,j):
    q = deque()
    graph[i][j] = 0
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx,ny))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i,j)
            cnt += 1
            
print(cnt)