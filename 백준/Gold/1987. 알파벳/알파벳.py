n,m=map(int,input().split())
visited = set()
graph = [list(input()) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

cnt = 0
def dfs(x,y,d):
    global cnt
    cnt = max(cnt, d)
    visited.add(graph[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] not in visited:            
                dfs(nx,ny,d+1)
    visited.remove(graph[x][y])
dfs(0,0,1)
print(cnt)