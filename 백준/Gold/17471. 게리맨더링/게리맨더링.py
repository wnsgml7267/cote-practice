from collections import deque
from itertools import combinations as cb
from collections import defaultdict

def bfs(x_list):
    start = x_list[0]
    sum = 0
    q = deque()
    q.append(start)
    visited = set([start])

    while q:
        x = q.popleft()
        sum += weight[x]
        for u in dic[x]:
            if u not in visited and u in x_list:
                visited.add(u)
                q.append(u)
    return sum, len(visited)

n = int(input())
weight = list(map(int,input().split()))
dic = defaultdict(list)
result = float('inf')

for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(1, arr[0]+1):
        dic[i].append(arr[j]-1)

ar = [i for i in range(1, n+1)]

for i in range(1, n//2+1):
    comb = list(cb(range(n), i))
    for co in comb:
        s, z = bfs(co)
        ss, zz = bfs([i for i in range(n) if i not in co])
        if z + zz == n:
            result = min(result, abs(s - ss))
if result != float('inf'):
    print(result)
else:
    print(-1)