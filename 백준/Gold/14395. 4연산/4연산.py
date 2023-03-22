from collections import deque, defaultdict

s, t = map(int,input().split())
visited = defaultdict(str)
q = deque()
q.append(s)
if s == t:
  print(0)
else:
  answer = -1
  while q:
    x = q.popleft()

    if x == t:
      answer = visited[x]
      break
    # 곱하기
    nx = x**2
    if 0 <= nx <= t and visited[nx] == "" and s != nx:
      visited[nx] = visited[x] + "*"
      q.append(nx)

    nx = x*2
    if 0 <= nx <= t and visited[nx] == "" and s != nx:
      visited[nx] = visited[x] + "+"
      q.append(nx)
    
    nx = 0
    if visited[nx] == "" and s != nx:
      visited[nx] = visited[x] + "-"
      q.append(nx)

    if x != 0:
        nx = 1
        if visited[nx] == "" and s != nx:
            visited[nx] = visited[x] + "/"
            q.append(nx)

  print(answer)