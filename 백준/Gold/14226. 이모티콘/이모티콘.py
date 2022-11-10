from collections import deque
n = int(input())
INF = 1001
graph = [[INF] * (n+1) for _ in range(n+1)]
graph[1][0] = 0 #이모티콘 갯수, 클립보드 갯수
q = deque()
q.append((1,0))

while q:
    x, y = q.popleft()
    #화면에 있는 이모티콘 복사 후 클립보드 저장
    if graph[x][x] == INF:
        graph[x][x] = graph[x][y] + 1
        q.append((x,x))
    #클립보드에 있는 이모티콘 모두 화면에 붙여넣기
    if x+y <= n and graph[x+y][y] == INF:
        graph[x+y][y] = graph[x][y] + 1
        q.append((x+y,y))
    #화면에 있는 이모티콘 중 하나를 삭제
    if 2 < x-1 <= n and graph[x-1][y] == INF:
        graph[x-1][y] = graph[x][y] + 1
        q.append((x-1,y))
print(min(graph[n]))