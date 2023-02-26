from collections import deque

# N x N 행열, K개의 소 위치, R개의 다리
N, K, R = map(int,input().split())
road_list = [[[] for _ in range(N)] for _ in range(N)] # 길 위치
cow_list = [] # 소 위치
count = 0 # 못 지나가는 쌍

dx = (1,-1,0,0)
dy = (0,0,1,-1)

def bfs(x1, y1):
    q = deque()
    q.append((x1,y1))
    visited[x1][y1] = True
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if not (nx,ny) in road_list[x][y]: # 길이 없는 곳만 탐색
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    

# 길 위치 저장
for i in range(R):
    a, b, a1, b1 = map(int,input().split())
    road_list[a-1][b-1].append((a1-1, b1-1))
    road_list[a1-1][b1-1].append((a-1, b-1))

# 소 위치 저장
for i in range(K):
    a, b = map(int,input().split())
    cow_list.append((a-1,b-1))

for i in range(len(cow_list)-1):
    visited = [[False] * N for _ in range(N)]

    bfs(cow_list[i][0], cow_list[i][1])

    for j in cow_list[i+1:]:
        if not visited[j[0]][j[1]]:
            count += 1
print(count)