R, C, N = map(int,input().split())
graph= []
for i in range(R):
    graph.append(list(input()))
dx = (1,-1,0,0)
dy = (0,0,1,-1)
if N == 1:
    for i in range(R):
        for j in range(C):
            print(graph[i][j], end = '')
        print()
else:
    N -= 1
    cnt = 1
    while (cnt <= N):
        # 1,2,3,0
        mode = cnt % 4
        if mode == 1: # X 설치
            for i in range(R):
                for j in range(C):
                    if graph[i][j] == '.':
                        graph[i][j] = 'X'
            
        elif mode == 2: # O 폭발
            for i in range(R):
                for j in range(C):
                    if graph[i][j] == 'O':
                        graph[i][j] = '.'
                        for m in range(4):
                            nx = dx[m] + i
                            ny = dy[m] + j
                            if 0 <= nx < R and 0 <= ny < C:
                                if graph[nx][ny] == 'X':
                                    graph[nx][ny] = '.'
        elif mode == 3: # O 설치
            for i in range(R):
                for j in range(C):
                    if graph[i][j] == '.':
                        graph[i][j] = 'O'
        elif mode == 0: # X 폭발
            for i in range(R):
                for j in range(C):
                    if graph[i][j] == 'X':
                        graph[i][j] = '.'
                        for m in range(4):
                            nx = dx[m] + i
                            ny = dy[m] + j
                            if 0 <= nx < R and 0 <= ny < C:
                                if graph[nx][ny] == 'O':
                                    graph[nx][ny] = '.'
        cnt += 1
    for k in range(R):
        for l in range(C):
            if graph[k][l] == 'X':
                graph[k][l] = 'O'
    for k in range(R):
        for l in range(C):
            print(graph[k][l], end = '')
        print()