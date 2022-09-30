import sys, heapq
n, m = map(int, input().split()) 
inf = float('inf')
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b, dis = map(int,input().split())
  graph[a].append((b, dis))
  graph[b].append((a, dis))
p, q = map(int,input().split())
homes = sorted(list(map(int, input().split())))
stores = list(map(int, input().split()))

dists = [inf] * (n+1)
heap = []

for i in stores:
  heapq.heappush(heap, (0, i))
  dists[i] = 0

while heap:
  distance, node = heapq.heappop(heap)

  if dists[node] < distance:
    continue

  for v, w in graph[node]:
    sum_distance = distance + w
    if dists[v] > sum_distance:
      dists[v] = sum_distance
      heapq.heappush(heap, (sum_distance, v))
    
tmp = homes[0]
answer = dists[tmp]
for i in homes:
  if dists[i] < answer and dists[i] != 0:
    tmp = i
    answer = dists[i]
print(tmp)