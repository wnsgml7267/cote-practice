n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

group = [[-1 for _ in range(m)] for _ in range(n)]

dir = ['L', 'R', 'U', 'D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def move(x, y, idx):
    global answer
    if group[x][y] != -1:
        if group[x][y] == idx:
            answer += 1
        return

    group[x][y] = idx
    i = dir.index(graph[x][y]) # 해당 그래프 좌표의 방향으로 이동
    move(x + dx[i], y + dy[i], idx)

idx = 0
answer = 0
for i in range(n):
    for j in range(m):
        move(i,j,idx)
        idx += 1
print(answer)