from collections import deque
n,k=map(int,input().split())
MAX=10**5
dis = [0]*(MAX+1)
q = deque()
q.append(n)
while q:
  a = q.popleft()
  if a == k: #동생 지점 도착했으면
    print(dis[a])
    break
  
  for i in (a-1, a+1, a*2):
    if 0 <= i <= MAX and not dis[i]:
      dis[i] = dis[a]+1
      q.append(i)