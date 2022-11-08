from collections import deque
n, m = map(int,input().split())
visited = [0 for _ in range(101)]
visit = [False for _ in range(101)]
graph = [i for i in range(101)]
for i in range(n+m):
    x, y = map(int,input().split())
    graph[x] = y
dice = [6,5,4,3,2,1]
q = deque()
q.append(1)
visit[1] = True
cnt = 0
while q:
    t = q.popleft()
    for i in range(6):
        td = t + dice[i]
        if 0 < td <= 100:
            if td != graph[td]:
                td = graph[td]
        if 0 < td <= 100 and visited[td] == 0 and visit[td] == False:
            q.append(td)
            visited[td] = visited[t] + 1
            visit[td] = True
print(visited[100])
