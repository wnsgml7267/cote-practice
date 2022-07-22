t=int(input())
dp = [[1,0,0,0,0,0,0,0,0,0] for i in range(65)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(2,65):
  for j in range(1,10):
    dp[i][j] = dp[i][j-1] + dp[i-1][j]
for i in range(t):
  n=int(input())
  print(sum(dp[n]))