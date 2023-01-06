#O는 빈 공간, X는 벽, I는 도연이, P는 사람이다
from collections import deque
n, m = map(int,input().split())
graph = []
dx, dy = (1,-1,0,0),(0,0,1,-1)
for i in range(n):
    graph.append(list(input()))
cnt = 0

def bfs(a,b):
    global cnt
    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != "X":
                if graph[nx][ny] == "O":
                    graph[nx][ny] = "a"
                    q.append((nx,ny))
                elif graph[nx][ny] == "P":
                    graph[nx][ny] = "a"
                    cnt += 1
                    q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            bfs(i,j)

if cnt == 0:
    print("TT")
else:
    print(cnt)
                            
                            
                
