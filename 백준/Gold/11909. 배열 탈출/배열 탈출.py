import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))
price = [[0]*n for i in range(n)]

for r in range(n):
  for c in range(n):
    if 0 > r-1 and 0 > c-1:
      continue
    pr_r, pr_c = int(1e9), int(1e9)
    if 0 <= r-1:
      pr_r = price[r-1][c] + (0 if graph[r][c] < graph[r-1][c] else graph[r][c] - graph[r-1][c] +1)
    if 0 <= c-1:
      pr_c = price[r][c-1] + (0 if graph[r][c] < graph[r][c-1] else graph[r][c] - graph[r][c-1] +1)
    price[r][c] = min(pr_r, pr_c)
print(price[n-1][n-1])