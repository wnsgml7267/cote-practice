from collections import deque
import sys

input = sys.stdin.readline

def bfs(x):
    q = deque()
    c = [0 for _ in range(n)]
    q.append(x)
    c[x] = 1
    cnt = 1
    while q:
        x = q.popleft()
        for nx in a[x]:
            if c[nx] == 0:
                cnt += 1
                c[nx] = 1
                q.append(nx)
    return cnt

n, m = map(int, input().split())
a = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    a[y-1].append(x-1)

ans = [0 for _ in range(n)]
for i in range(n):
    ans[i] = bfs(i)
for i in range(n):
    if ans[i] == max(ans):
        print(i+1, end=' ')