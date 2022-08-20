graph = [list(map(int,list(input()))) for _ in range(8)]
visited = [[False] * 7 for _ in range(8)]
domino = [[False] * 7 for _ in range(7)]

def rec_fun(x, y):
  if x == 8: return 1
  count = 0
  nx, ny = x, y + 1
  if ny == 7:
    nx, ny = x + 1, 0
  if visited[x][y]:
    return rec_fun(nx,ny)
  else:
    now = graph[x][y]
    visited[x][y] = True
    for dx, dy in ((0, 1), (1, 0)):
      mx, my = x + dx, y + dy
      if mx in range(8) and my in range(7):
        pair = graph[mx][my]

        if not visited[mx][my] and not domino[now][pair]:
          domino[now][pair] = domino[pair][now] = True
          visited[mx][my] = True

          count += rec_fun(nx, ny)

          visited[mx][my] = False
          domino[now][pair] = domino[pair][now] = False
    visited[x][y] = False
    return count
print(rec_fun(0, 0))
