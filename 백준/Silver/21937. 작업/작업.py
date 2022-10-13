import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int,input().split()) #작업 개수, 작업 정보 개수
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
cnt = 0
for i in range(m):
  a, b =map(int,input().split())
  graph[b].append(a)
x = int(input()) #끝내야 할 작업
def dfs(x):
  global cnt
  visited[x] = True
  for i in range(len(graph[x])):
    tmp = graph[x][i]
    if not visited[tmp]:
      cnt += 1
      dfs(tmp)
  return cnt
print(dfs(x))

