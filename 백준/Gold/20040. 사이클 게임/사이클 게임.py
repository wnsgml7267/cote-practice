import sys
input = sys.stdin.readline
n, m = map(int,input().split()) # 점의 개수, 간선

edges = [] # 간선 정보
parent = [0] * n
cnt = 0 # 선 그은 횟수
ans = 0 # 결과 값

for i in range(m):
    a, b = map(int,input().split())
    edges.append((a, b))

for i in range(n):
    parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a, b = edges[i]
    cnt += 1
    if find_parent(parent, a) == find_parent(parent, b):
        ans = cnt
        break
    else:
        union_parent(parent, a, b)
print(ans)