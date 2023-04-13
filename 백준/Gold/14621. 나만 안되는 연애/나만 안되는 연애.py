from heapq import heappop, heappush

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    aRoot = find(x)
    bRoot = find(y)
    if aRoot < bRoot:
        parents[bRoot] = aRoot
    else:
        parents[aRoot] = bRoot
    
n, m = map(int,input().split())
uni = [0] + list(input().split())

bool = True
heap = []
total = 0
parents = [-1] * (n+1)
visited = [False] * (n+1)
for i in range(1, n+1):
    parents[i] = i
for i in range(m):
    u, v, cost = map(int,input().split())
    heappush(heap, (cost, u, v))

while(heap):
    cost, x, y = heappop(heap)

    if find(x) != find(y) and uni[x] != uni[y]:
        visited[x] = True
        visited[y] = True
        union(x, y)
        total += cost
if visited.count(False) > 1:
    bool = False
if bool:
    print(total)
else:
    print(-1)