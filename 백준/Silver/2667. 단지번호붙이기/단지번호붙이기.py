import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = []
num = []

for i in range(n):
  graph.append(list(map(int, input().strip())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x, y):
  if x < 0 or x >= n or y < 0 or y >= n:
    return False
  #1이면 count 증가 (집이 있으므로)
  if graph[x][y] == 1:
    global count
    count += 1
    graph[x][y] = 0
    for i in range(4):
      #인접한 가로 세로 탐색
      nx = x + dx[i]
      ny = y + dy[i]
      DFS(nx, ny)
    return True
  return False
count = 0
result = 0

for i in range(n):
  for j in range(n):
    if DFS(i, j) == True:
      num.append(count)
      #단지 수
      result += 1
      count = 0
num.sort()
print(result)
for i in range(len(num)):
  print(num[i])