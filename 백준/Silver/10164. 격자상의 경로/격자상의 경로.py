import sys
input = sys.stdin.readline

n, m, k = map(int,input().split()) #행, 열, O
dp = [[0]*(m+1) for i in range(n+1)]
dp[0][1] = 1
sx = (k-1) // m + 1
sy = k - (sx-1) * m
for i in range(1, n+1):
  for j in range(1, m+1):
    dp[i][j] = dp[i-1][j] + dp[i][j-1]

if k == 0:
  print(dp[n][m])
else:
  print(dp[sx][sy] * dp[n-sx+1][m-sy+1])

