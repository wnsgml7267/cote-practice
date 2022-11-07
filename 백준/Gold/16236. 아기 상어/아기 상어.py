from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

#먹이를 찾으러 간 아기 상어의 위치와 걸린 시간 리스트 리턴
def bfs(i,j,shark_size):
    q = deque()
    q.append((i,j))
    dis = [[0]*n for _ in range(n)] #거리(=시간(초))
    visited = [[0]*n for _ in range(n)] #방문
    visited[i][j] = 1 #방문 확인
    eat = [] #먹이(좌표,거리(시간))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= shark_size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    dis[nx][ny] = dis[x][y] + 1
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0: #상어 크기보다 작은 먹이
                        eat.append([nx,ny,dis[nx][ny]])
    return sorted(eat, key = lambda x: (-x[2], -x[0], -x[1])) #거리, 위, 왼쪽 순서

dx, dy = (1,-1,0,0), (0,0,1,-1)
x,y,shark_size = 0,0,2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j
cnt, time = 0, 0 #먹은 횟수, 걸린 시간

#bfs 먹이 탐색할 때마다 조건 확인
while True:
    tmp = bfs(x,y,shark_size)
    if len(tmp) == 0: #먹이가 없으면
        break
    nx, ny, size = tmp.pop()
    time += size #시간 누적
    graph[x][y], graph[nx][ny] = 0, 0 #상어 위치와 상어가 이동한 위치 값 초기화
    x, y = nx, ny #상어 위치 초기화
    cnt += 1
    if cnt == shark_size: #먹이 먹은 횟수와 상어 크기가 같으면 상어 크기 증가
        shark_size += 1
        cnt = 0 #먹이 먹은 횟수 초기화
print(time)
