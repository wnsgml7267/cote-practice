from collections import deque
def solution(maps):
    answer = 0
    q = deque()
    visited = [[False]*len(maps[0]) for i in range(len(maps))]
    visited[0][0] = True
    q.append([0,0])
                
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx,ny])
                maps[nx][ny] = maps[x][y] + 1
    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]

    return answer
