from collections import deque
n, m, k = map(int,input().split())
graph = [[0]*m for _ in range(n)]

for i in range(k):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1

dx, dy = (1,-1,0,0), (0,0,1,-1)
q = deque()
max_cnt = 0

def bfs(i,j):
    global max_cnt, cnt
    q.append((i,j))
    graph[i][j] += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    cnt += 1
                    q.append((nx,ny))
    if max_cnt < cnt:
        max_cnt = cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 1
            bfs(i,j)
print(max_cnt)

