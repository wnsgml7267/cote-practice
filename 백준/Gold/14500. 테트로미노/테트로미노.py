import sys; input=sys.stdin.readline
def dfs(r,c,idx,total):
  global ans
  if ans >= total + max_val * (3-idx):
    return
  if idx == 3:
    ans = max(ans, total)
    return
  else:
    for i in range(4):
      nx = r + dx[i]
      ny = c + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
        if idx == 1:
          visited[nx][ny] = 1 #방문 체크
          dfs(r, c, idx + 1, total + graph[nx][ny])          
          visited[nx][ny] = 0
        visited[nx][ny] = 1
        dfs(nx,ny,idx+1, total+graph[nx][ny])
        visited[nx][ny]=0

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [([0] * m) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 0
max_val = max(map(max, graph))
#브루트포싱
for i in range(n): 
  for j in range(m):
    visited[i][j] = 1 #방문
    dfs(i,j,0,graph[i][j])
    visited[i][j] = 0 #방문 해제
print(ans)