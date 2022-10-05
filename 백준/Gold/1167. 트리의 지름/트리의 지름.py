import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
#정점의 개수
V = int(input())
#트리
tree = [[] for _ in range(V+1)]
distance1 = [0 for _ in range(V+1)]
distance2 = [0 for _ in range(V+1)]
#정점 번호, 연결된 간선, 거리
for _ in range(V):
  info = list(map(int, input().split()))
  #트리 구성
  for i in range(1,len(info)-2,2):
    tree[info[0]].append([info[i], info[i+1]])

def dfs(node, distance):
  #i=연결된 간선, d=거리
  for i, d in tree[node]:
    if distance[i] == 0:
      distance[i] = distance[node] + d
      dfs(i,distance)
#노드 각 거리 확인
dfs(1, distance1)
#distance1의 최댓값(최대 거리)의 인덱스 
max_idx = distance1.index(max(distance1))
#최댓값의 인덱스에서 dfs함수를 한 번 더 돌려서 가장 긴 길이 즉, 지름을 구함
dfs(max_idx, distance2)
distance2[max_idx]=0
print(max(distance2))
