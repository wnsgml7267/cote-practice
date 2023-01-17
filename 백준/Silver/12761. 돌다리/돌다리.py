from collections import deque
#힘a, b, 동규, 주미
a,b,n,m=map(int,input().split())
visited=[False for _ in range(100001)]
graph=[0 for _ in range(100001)]
dx=(1,-1,a,-a,b,-b,a,b)
q=deque()
q.append(n)
visited[n] = True
while q:
  x = q.popleft()
  if x == m:
    break
  
  for i in range(8):
    if i > 5:
      nx = dx[i] * x
    else:
      nx = dx[i] + x
    if 0 <= nx < 100001:
      if visited[nx] == False:
        visited[nx] = True
        graph[nx] = graph[x] + 1
        q.append(nx)
  
print(graph[m])