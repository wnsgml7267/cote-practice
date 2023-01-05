# 늑대 : v 양 : k 공백 : . 벽 : #
from collections import deque
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
dx, dy = (1,-1,0,0), (0,0,1,-1)
wolf = 0 # 총 늑대 수
sheep = 0 # 총 양의 수

def bfs(a,b):
    global wolf, sheep
    q = deque()
    q.append((a,b))
    v, k = 0, 0
    if graph[a][b] == "v":
        v += 1
    elif graph[a][b] == "k":
        k += 1
    graph[a][b] = "#"
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != "#":
                if graph[nx][ny] == "v":
                    v += 1
                elif graph[nx][ny] == "k":
                    k += 1
                graph[nx][ny] = "#"
                q.append((nx,ny))
    if v >= k:
        wolf += v
    else:
        sheep += k
        
for i in range(n):
    for j in range(m):
        if graph[i][j] == "." or graph[i][j] == "v" or graph[i][j] == "k":
            bfs(i,j)
print(sheep, wolf)