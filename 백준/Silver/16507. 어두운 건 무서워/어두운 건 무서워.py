import sys
input = sys.stdin.readline
r,c,q = map(int,input().split())
graph = []
sum_graph = [[0]*(c+1) for _ in range(r+1)]
for i in range(r):
  graph.append(list(map(int,input().split())))

for i in range(1, r+1):
    for j in range(1, c+1):
        sum_graph[i][j] = sum_graph[i-1][j]+sum_graph[i][j-1]+graph[i-1][j-1]-sum_graph[i-1][j-1]
for i in range(q):
  r1, c1, r2, c2 = map(int,input().split())
  total = sum_graph[r2][c2]-sum_graph[r1-1][c2]-sum_graph[r2][c1-1]+sum_graph[r1-1][c1-1]
  print(total // ((r2 - r1 + 1 ) * (c2 - c1 + 1)))

  
  