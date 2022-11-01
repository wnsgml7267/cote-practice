from collections import deque
n, m = map(int,input().split())
graph = []
visited = [[0]*m for _ in range(n)]

for i in range(n):
    graph.append(list(input()))
dx, dy = (1,-1,0,0), (0,0,1,-1)
q = deque()

def search(a,b):
    global max_dis
    visited[a][b] = 1
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    if max_dis < visited[nx][ny]:
                        max_dis = visited[nx][ny]
                    q.append((nx,ny))

max_dis = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            search(i,j)
print(max_dis-1)
