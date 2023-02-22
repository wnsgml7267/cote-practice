import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int, input().split())

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

parents = [i for i in range(n+1)]
for i in range(m):
    c, a, b = map(int,input().split())
    if c == 0:
        union(a,b)
    elif c == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")