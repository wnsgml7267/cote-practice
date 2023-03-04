from collections import deque

n = int(input())
graph = []
shark_x = 0
shark_y = 0
shark_size = 2
eat = 0
dx, dy = (1,-1,0,0), (0,0,1,-1)
eating = []
answer = 0
for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0

def check():
    global shark_size
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and shark_size > graph[i][j] :
                return True
    return False


def bfs(a, b):
    global shark_size, eating
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    eating = []
    while q:
        x, y = q.popleft()
        # 먹이를 찾았을 때
        if graph[x][y] != 0 and graph[x][y] < shark_size:
            # 거리, x축, y축 저장
            eating.append([visited[x][y] - 1, x, y])

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 지나갈 수 있으면 지나가기
                if graph[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return eating
    
while True:
    if(check()):
        bfs(shark_x, shark_y)
        if len(eating) == 0:
            break
        eating.sort()
        answer += eating[0][0]
        shark_x = eating[0][1]
        shark_y = eating[0][2]
        graph[shark_x][shark_y] = 0
        eat += 1
        # 레벨업
        if shark_size == eat:
            shark_size += 1
            eat = 0
    else:
        break
print(answer)