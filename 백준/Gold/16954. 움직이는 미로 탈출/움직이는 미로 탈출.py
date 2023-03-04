from collections import deque

# 8 x 8 행렬
graph = []
for i in range(8):
    graph.append(list(input()))
# 하, 상, 우, 좌, 대각 x 4, 제자리
dx = (1,-1,0,0,1,1,-1,-1,0)
dy = (0,0,1,-1,1,-1,1,-1,0)
visited = [[False for _ in range(8)] for _ in range(8)] # 방문 체크
wall = deque() # 벽이 있는 좌표
answer = 0 # 도착 여부
wall_count = 0 # 남아있는 벽의 개수

# 벽 좌표 넣기
for i in range(8):
    for j in range(8):
        if graph[i][j] == '#':
            wall.appendleft((i,j))

def bfs(a, b):
    global answer, visited
    q = deque()
    q.append((a,b))
    
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            # visited[x][y] = True
            if x == 0 and y == 7:
                answer = 1
                return
            if graph[x][y] == '#':
                continue

            for i in range(9):
                nx, ny = dx[i] + x, dy[i] + y
                if 0 <= nx < 8 and 0 <= ny < 8 and visited[nx][ny] == False and graph[nx][ny] != '#':
                    visited[nx][ny] = True
                    q.append((nx,ny))

        # 내려야 할 벽이 존재한다면
        if wall:
            visited = [[False for _ in range(8)] for _ in range(8)] # 방문 체크 초기화
            for _ in range(len(wall)):
                # 한 번 이동했으니 벽을 내려준다.
                xx, yy = wall.popleft()
                if xx < 7:
                    graph[xx][yy] = '.'
                    graph[xx+1][yy] = '#'
                    wall.append((xx+1,yy))
                elif xx == 7:
                    graph[xx][yy] = '.'

# 왼쪽 아래 출발
bfs(7,0)

print(answer)