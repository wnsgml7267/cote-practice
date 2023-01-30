from collections import deque

t = int(input())
dx, dy = (1,-1,0,0), (0,0,1,-1)

for _ in range(t):
    graph = []
    cnt = 0
    x, y = map(int,input().split())
    
    def bfs(a,b):
        graph[a][b] = "."
        
        q = deque()
        q.append((a,b))
   
        while q:
            u,v = q.popleft()
            for k in range(4):
                nx, ny = dx[k] + u, dy[k] + v
                if 0 <= nx < x and 0 <= ny < y:
                    if graph[nx][ny] == "#":
                        graph[nx][ny] = '.'
                        q.append((nx,ny))
    for _ in range(x):
        graph.append(list(input()))
    for i in range(x):
        for j in range(y):
            if graph[i][j] == "#":
                bfs(i,j)
                cnt += 1
    print(cnt)