n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))
cnt = 0
#z : 가로(0), 세로(1), 대각선(2)
def dfs(x,y,z):
  global cnt

  if [x,y] == [n-1,n-1]:
    cnt += 1
    return

  #[대각선 이동] : 가로, 세로 대각선일 경우
  if x+1 < n and y+1 < n:
    if graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
      dfs(x+1,y+1,2)
  #[가로 이동] : 가로, 대각선일 경우
  if z == 0 or z == 2:
    if y+1 < n:
      if graph[x][y+1] == 0:
        dfs(x,y+1,0)
  #[세로 이동] : 세로, 대각선일 경우
  if z == 1 or z == 2:
    if x+1 < n:
      if graph[x+1][y] == 0:
        dfs(x+1,y,1)
dfs(0,1,0)
print(cnt)