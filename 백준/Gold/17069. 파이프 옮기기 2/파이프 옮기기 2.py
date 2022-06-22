n = int(input())
# (1,1) ~ (n,n)
graph = [[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]
# 3차원배열 [x][y][m] m=0,1,2(=가로,세로,대각선 횟수)
dp = [[[0]*3 for _ in range(n+1)] for _ in range(n+1)]
#시작점(파이프 끝지점)
dp[1][2][0] = 1
for i in range(1, n+1):
  for j in range(1, n+1):
    #가로축 끝이 아니고, 다음 가로축이 벽이 아닐 경우
    if j < n and not graph[i][j+1]:
      #가로로 갈 수 있는 곳은 대각선과 가로
      dp[i][j+1][0] += dp[i][j][0] + dp[i][j][2]
    #세로축 끝이 아니고, 다음 세로축이 벽이 아닐 경우
    if i < n and not graph[i+1][j]:
      #세로로 갈 수 있는 곳은 세로와 대각선
      dp[i+1][j][1] += dp[i][j][1] + dp[i][j][2]
    #세로,가로축 끝이 아니고, 가로, 세로, 대각선 중 벽이 아닐 경우
    if i < n and j < n and not (graph[i][j+1] or graph[i+1][j] or graph[i+1][j+1]):
      #대각선으로 갈 수 있는 곳은 가로, 세로, 대각선
      dp[i+1][j+1][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
print(sum(dp[n][n]))