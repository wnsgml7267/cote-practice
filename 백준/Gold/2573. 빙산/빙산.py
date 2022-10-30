from collections import deque
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = (1,-1,0,0), (0,0,1,-1)
day = 0
check = False
q = deque()
def bfs(a,b):
    q.append((a,b))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

#빙산이 분리될 때까지
while True:
    visited = [[False]*m for _ in range(n)] #방문 초기화
    count =  [[0]*m for _ in range(n)] #주변 0 개수
    result = []
    #분리된 빙산 개수 판단
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
    #주변 0의 개수만큼 빙산 녹임            
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    #빙산이 다 녹으면
    if len(result) == 0:
        break
    #분리된 빙산이 있으면
    if len(result) >= 2:
        check = True
        break
    #녹을 때마다 날짜 증가
    day += 1
if check:
    print(day)
else:
    print(0)
