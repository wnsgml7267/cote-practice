import sys
input = sys.stdin.readline
def width(x,n):
  for i in range(9):
    if graph[x][i] == n:
      return False
  return True
def height(y,n):
  for i in range(9):
    if graph[i][y] == n:
      return False
  return True

def rect(x,y,n):
  dx, dy = x // 3 * 3, y // 3 * 3
  for i in range(3):
    for j in range(3):
      if graph[dx+i][dy+j] == n:
        return False
  return True

def back(n):
  if len(zero) == n: # 빈 공간 다 채웠을 경우
    for k in range(9):
      print(*graph[k])
    exit(0)

  x, y = zero[n][0], zero[n][1]

  for i in range(1, 10):
    if width(x, i) and height(y, i) and rect(x, y, i):
      graph[x][y] = i
      back(n + 1)
      graph[x][y] = 0

graph = []
zero = []
for i in range(9):
  graph.append(list(map(int,input().split())))
  for j in range(9):
    if graph[i][j] == 0:
      zero.append((i,j))
back(0)