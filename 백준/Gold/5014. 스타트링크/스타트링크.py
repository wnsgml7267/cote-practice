from collections import deque
f,s,g,u,d = map(int,input().split())
visited = [0] * (f+1)
q = deque()
q.append(s)
answer = "use the stairs"
visited[s] = 1
while q:
  floor = q.popleft()
  if floor == g:
    answer = visited[floor] - 1
    break
  floor_up = floor + u
  floor_down = floor - d
  if floor_up <= f and visited[floor_up] == 0:
    visited[floor_up] = visited[floor] + 1
    q.append(floor_up)
  if floor_down >= 1 and visited[floor_down] == 0:
    visited[floor_down] = visited[floor] + 1
    q.append(floor_down)
print(answer)