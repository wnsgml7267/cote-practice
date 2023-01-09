from collections import deque

graph = []
for i in range(5):
    graph.append(list(map(int,input().split())))
r, c = map(int,input().split())

dx,dy=(1,-1,0,0),(0,0,1,-1)

visited = [[0]*5 for _ in range(5)]
def bfs(a,b):
    cnt = -1
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny]==0:
                if graph[nx][ny] == 1:
                    cnt = visited[x][y]
                    return cnt
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                elif graph[nx][ny] == -1:
                    visited[nx][ny] = -1
    return cnt
print(bfs(r,c))