from collections import deque
n = int(input())
#출발(r1,c1), 도착(r2,c2)
r1, c1, r2, c2 = map(int,input().split())
visited = [[0] * n for _ in range(n)]
visited[r1][c1] = 1
q = deque()
q.append((r1,c1))
dx = (0,0,2,2,-2,-2)
dy = (2,-2,-1,1,-1,1)
while q:
    x, y = q.popleft()

    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if nx == r2 and ny == c2:
                visited[nx][ny] = visited[x][y] + 1    
                break
            else:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

if visited[r2][c2] == 0:
    print(-1)
else:
    print(visited[r2][c2]-1)