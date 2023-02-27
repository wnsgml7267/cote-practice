n = int(input())
graph = [[0 for _ in range(101)] for _ in range(101)]
for i in range(n):
    a, b = map(int,input().split())
    for j in range(a, a+10):
        for k in range(b, b+10):
            graph[j][k] = 1
cnt = 0
dx, dy = (1,-1,0,0), (0,0,1,-1)
for i in range(101):
    for j in range(101):
        if graph[i][j] == 1:
            for k in range(4):
                nx, ny = dx[k] + i, dy[k] + j
                if 0 <= nx < 101 and 0 <= ny < 101:
                    if graph[nx][ny] == 0:
                        cnt += 1
print(cnt)