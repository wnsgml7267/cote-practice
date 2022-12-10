import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

graph = []
R, C = map(int,input().split())
for i in range(R):
    graph.append(list(input()))
visited = [[False] * C for _ in range(R)]

dx = (1,-1,0,0)
dy = (0,0,1,-1)

v_cnt = 0
o_cnt = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and not visited[i][j]:
            o, v = 0, 0
            if graph[i][j] == 'v':
                v = 1
            elif graph[i][j] == 'o':
                o = 1                
            visited[i][j] = True
            q = deque()
            q.append((i,j))
            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != '#':
                        if graph[nx][ny] == 'v':
                            v += 1
                        elif graph[nx][ny] == 'o':
                            o += 1
                        visited[nx][ny] = True
                        q.append((nx,ny))
            if o > v:
                v = 0
            else:
                o = 0
            v_cnt += v
            o_cnt += o
            
print(o_cnt, v_cnt)            
