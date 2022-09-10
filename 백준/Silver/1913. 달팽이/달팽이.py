n = int(input())
m = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
x, y = n//2, n//2
num = 1
le = 0
coordinate = [x+1,y+1]
graph[x][y] = num

while True:
  for i in range(4):
      for _ in range(le):
        x += dx[i]
        y += dy[i]
        num += 1
        graph[x][y] = num
        if num == m:
          coordinate = [x+1, y+1]
  if x == y == 0:
    break
  x -= 1
  y -= 1
  le += 2
for i in range(n):
  print(*graph[i])
print(*coordinate)
    