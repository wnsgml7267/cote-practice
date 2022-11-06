from collections import deque
n, m = map(int,input().split())
q = deque()
q.append(n)
visited = [-1] * 100001
visited[n] = 0
while q:
    x = q.popleft()
    #도착시
    if x == m:
        print(visited[x])
        break
    #0초 후 x*2 이동
    if 0 <= x*2 <= 100000 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        q.append(x*2)
    #1초 후 x-1 이동
    if 0 <= x-1 <= 100000 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
    #1초 후 x+1 이동
    if 0 <= x+1 <= 100000 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)