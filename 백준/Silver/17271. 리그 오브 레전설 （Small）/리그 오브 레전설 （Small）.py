INF = 1000000007
n, m = map(int,input().split())
dp = [0] * (n+1)
dp[0] = 1 # 0번 스킬 쓰는 경우 : 한 번
for i in range(1, n+1):
    dp[i] = dp[i-1] % INF
    if i >= m:
      dp[i] += dp[i-m] % INF
print(dp[n] % INF)