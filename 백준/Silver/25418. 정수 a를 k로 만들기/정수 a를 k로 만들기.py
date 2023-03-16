from collections import deque
a, k = map(int, input().split())
visited = [10**9] * (2 * k + 1)
def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = 0
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        elif x > k:
            continue
        if visited[x*2] == 10**9:
            q.append(x*2)
            visited[x*2] = visited[x]+1
        if visited[x+1] == 10**9:
            q.append(x+1)
            visited[x+1] = visited[x]+1
          
    

bfs(a)