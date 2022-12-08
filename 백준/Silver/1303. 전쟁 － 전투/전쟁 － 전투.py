from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

w_count = 0
b_count = 0

graph = []
m, n = map(int,input().split())
for i in range(n):
    graph.append(list(input()))

visited = [[0] * m for _ in range(n)]

dx = (1,-1,0,0)
dy = (0,0,1,-1)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W' and visited[i][j] == 0:
            visited[i][j] = 1
            q = deque()
            q.append((i,j))
            w = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'W' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        w += 1
                        q.append((nx,ny))
            w_count += w**2
        elif graph[i][j] == 'B' and visited[i][j] == 0:
            visited[i][j] = 1
            q = deque()
            q.append((i,j))
            b = 1 
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'B' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        b += 1
                        q.append((nx,ny))
            b_count += b**2        
print(w_count, b_count)




