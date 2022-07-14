n = int(input())
dp = []
answer = 0
for i in range(n):
  dp.append(list(map(int,input().split())))
for i in range(1,n):
  for j in range(len(dp[i])):
    if j == 0: #첫 지점이면
      dp[i][j] = dp[i-1][j]+dp[i][j]
    elif j == len(dp[i])-1: #끝 지점이면
      dp[i][j] = dp[i-1][j-1]+dp[i][j]
    else: #사이 지점이면
      dp[i][j] = max(dp[i][j]+dp[i-1][j-1], dp[i][j]+dp[i-1][j] )
print(max(map(max, dp)))