n = int(input())
dp = [0] * (n+1+4)
# 창영 : 0, 상근 : 1
# 창영, 상근, 창영, 상근 승리
dp[1], dp[2], dp[3], dp[4] = 0, 1, 0, 1
for i in range(5, n+1):
    if dp[i-1] and dp[i-3] and dp[i-4]:
        dp[i] = 0
    else:
        dp[i] = 1
if dp[n]: print("SK")
else: print("CY")