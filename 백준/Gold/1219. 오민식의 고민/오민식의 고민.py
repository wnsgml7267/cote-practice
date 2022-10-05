from collections import deque
import sys
input = sys.stdin.readline
INF = -int(1e9)

def BF(start, end):
  array = [INF for _ in range(N)]
  array[start] = T_array[start] #제자리일 경우

  #도착 가능 여부 판단
  for _ in range(N-1): #한 싸이클 돌아서 갱신 (N-1)
    for u,v,w in graph:
      if array[u] != INF and array[u] + w > array[v]:
        array[v] = array[u] + w
  if array[end] == INF: #도착 불가
    return 'gg'
  
  #무한 루프 판단
  for u,v,w in graph:
    if array[u] != INF and array[u] + w > array[v]: #한 번 더 돌았는데 갱신되면 무한 싸이클.
      if bfs(v, end): #도착도 가능하면 Gee
        return 'Gee'

  return array[end] #최대 액수 리턴

def bfs(start, end):
  q = deque()
  q.append(start)
  visited = [False]*N
  visited[start] = True
  while q:
    now = q.popleft()
    if now == end:
      return True
    for a,b,c in graph:
      if a == now:
        if not visited[b]:
          visited[b] = True
          q.append(b)
  return False

#도시 수(0~N-1), 시작, 도착, 교통수단 수
N, start, end, M = map(int,input().split())
graph = []
for _ in range(M):
  S, E, P = map(int,input().split()) #출발점, 도착점, 교통비
  graph.append([S, E, -P])
T_array = list(map(int,input().split()))
for i in range(M):
  graph[i][2] = T_array[graph[i][1]] + graph[i][2] #교통비 + 수입
print(BF(start, end))
