import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx, dy = (1,-1,0,0), (0,0,1,-1)
ans = []

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                # 치즈가 아닌 부분만 q에 추가
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                # 가장자리 치즈부분 이므로, q에 넣지않고, 방문 체크와 치즈를 녹인다.
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt
            
time = 0
while 1:
    time += 1
    visited = [[0]*m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break
print(time-1)
print(ans[-2])
