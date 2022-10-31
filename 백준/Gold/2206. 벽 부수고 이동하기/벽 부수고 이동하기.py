from collections import deque
n, m = map(int,input().split())
graph = []
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
for i in range(n):
    graph.append(list(map(int,input())))
dx, dy = (1,-1,0,0), (0,0,1,-1)
q = deque()
def bfs(a,b,c):
    q.append((a,b,c))

    while q:
        x, y, z = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                #벽이고, 벽을 한 번도 부수지 않았을 경우
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx,ny,1))
                #벽이 아니고, 방문하지 않았을 경우
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx,ny,z))
    return -1
print(bfs(0,0,0))
