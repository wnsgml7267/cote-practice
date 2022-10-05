import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


#노드의 개수
N = int(input())

tree= [[] for _ in range(N+1)]
distance1 = [0 for _ in range(N+1)]
distance2 = [0 for _ in range(N+1)]

#부모 노드, 자식 노드, 거리
for _ in range(N-1):
  link = list(map(int, input().split()))
  tree[link[0]].append([link[1], link[2]])
  tree[link[1]].append([link[0], link[2]])

def dfs(node, distance):
  #i=노드, d=거리
  for i, d in tree[node]:
    if distance[i] == 0:
      distance[i] = distance[node] + d
      dfs(i, distance)

dfs(1,distance1)
#distance1[1]=0
max_idx = distance1.index(max(distance1))
dfs(max_idx, distance2)
distance2[max_idx] = 0
print(max(distance2))
