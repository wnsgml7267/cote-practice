import sys
import heapq
from collections import defaultdict
n, m = map(int, input().split()) #정점 개수, 간선 개수
graph = defaultdict(list)
for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b, c])
  graph[b].append([a, c])
P,Q = map(int,input().split()) #집, 편의점 개수
homes = sorted(list(map(int, input().split()))) #집
stores = list(map(int, input().split())) #편의점

dists = [1_000_000_000_001] * (n+1)
min_dist, answer = 1_000_000_000_001, 0

min_dists = [1_000_000_000_001] * (n+1)
heap = []
for i in stores: #편의점 정점
  heapq.heappush(heap, (0, i))
  min_dists[i] = 0

while heap:
  d, node = heapq.heappop(heap) #거리, 현재 정점
  if node in homes: #현재 정점이 집에 도착하면
    break
  if min_dists[node] < d:
    continue
  for v, w in graph[node]: #현재 정점에서 다른 곳의 정점, 거리
    alt = d + w  #거리 합
    if min_dists[v] > alt and not v in stores: #집에 도달하지 않고 alt가 최소거리면
      min_dists[v] = alt
      heapq.heappush(heap, (alt, v))
    dists[v] = min(dists[v], min_dists[v]) #각 정점까지 도달하는 최소거리
tmp = homes[0]
answer = dists[tmp]
for i in homes:
  if dists[i] < answer: #앞 보다 최소거리가 작으면
    tmp = i
    answer = dists[i]
print(tmp)