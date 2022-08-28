from collections import deque
n,m = map(int,input().split()) #유저, 친구관계 수
graph = [deque() for i in range(n+1)]
answer = []
for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(graph,start):
  cnt = [0]*(n+1)
  visited = [start]
  queue = deque()
  queue.append(start)
  while queue:
    a = queue.popleft()
    for i in graph[a]:
      if i not in visited:
        cnt[i] = cnt[a] + 1
        visited.append(i)
        queue.append(i)
  return sum(cnt)
for i in range(1,n+1):
  answer.append(bfs(graph,i))
print(answer.index(min(answer))+1)
        