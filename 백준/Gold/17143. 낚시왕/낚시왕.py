import sys
input = sys.stdin.readline
from collections import deque

R, C, M = map(int,input().split()) # 행, 열, 상어의 수
graph = [[[0]*3 for _ in range(C)] for _ in range(R)]
for i in range(M):
    r, c, speed, direction, size = map(int,input().split())
    graph[r-1][c-1] = [speed, direction-1, size]
shark_list = deque()
answer = 0
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 상, 하, 우, 좌

def shark_move():
    global R, C
    new_shark = deque()
    while shark_list:
        x, y = shark_list.popleft()
        # 상어 이동시키기
        s = graph[x][y][0] # 상어 속력
        d = graph[x][y][1] # 상어 방향
        z = graph[x][y][2] # 상어 크기
        graph[x][y] = [0, 0, 0] # 현재 상어 위치 없앰
        dist = s
        while 0 < dist:
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            # 범위 내 이동(방향 전환 X)
            if 0 <= nx < R and 0 <= ny < C:
                x, y = nx, ny
                dist -= 1 # 속력 감소
            # 벽과 충돌(방향 전환 O)
            else:
                if d == 0 or d == 2:
                    d += 1
                else:
                    d -= 1
        new_shark.append([x, y, s, d, z])

    while new_shark:
        x1, y1, spd1, dir1, sz1 = new_shark.popleft()
        if graph[x1][y1][2] > sz1: # 기존에 있는 상어가 더 크면 그냥 넘어감
            continue
        else:
            graph[x1][y1] = [spd1, dir1, sz1]

# C열 만큼 사람이 이동
for i in range(C):
    for j in range(R):
        if graph[j][i][2] > 0: # 상어가 존재하면 (상어 크기)
            answer += graph[j][i][2] # 상어 잡기
            graph[j][i] = [0,0,0] # 바다에서 상어 제거
            break # 다음 열 이동
    shark_list = deque()
    # 상어 이동 시키기
    for j in range(R):
        for k in range(C):
            if graph[j][k][2] > 0: # 상어가 있으면 
                shark_list.append((j,k))
    shark_move()

print(answer)