import sys
sys.setrecursionlimit(10**9)
n, m, k = map(int,input().split())
visited = [[False] * m for _ in range(n)]
count = 0
depth = []
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            visited[j][k] = True

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y, d):
    visited[x][y] = True
    d += 1
    
    for i in range(4):        
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False:
                
                d = dfs(nx, ny, d)
    return d
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            d = 0
            depth.append(dfs(i,j,d))
            count += 1
depth.sort()
print(count, *depth)