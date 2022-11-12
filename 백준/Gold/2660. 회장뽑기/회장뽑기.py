from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
while 1:
    a, b = map(int,input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(t):
    q = deque()
    q.append(t)
    visited = [-1] * (n+1)
    visited[t] = 0

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)
    return max(visited)

score = 50
for i in range(1,n+1):
    tmp = bfs(i)
    if tmp < score:
        score = tmp
        arr = [i]
    elif tmp == score:
        arr.append(i)
arr.sort()
print(score, len(arr))
print(*arr)
