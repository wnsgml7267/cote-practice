n = int(input())
arr = list(map(int,input().split()))
# dp[1~n 인덱스][올바른 등식(0~20) 중 현재까지 구한 수]
dp = [[0 for _ in range(21)] for _ in range(n)]
dp[0][arr[0]] = 1
for i in range(1,n-1): # 마지막 arr값은 value라서 뺌
    for j in range(21):
        if dp[i-1][j]: # 이전 인덱스까지 올바른 등식이면
            # 이전까지 구한 수 + 현재 수 <= 20
            if j + arr[i] <= 20: dp[i][j+arr[i]] += dp[i-1][j]
            # 이전까지 구한 수 - 현재 수 >= 0
            if j - arr[i] >= 0: dp[i][j-arr[i]] += dp[i-1][j]
print(dp[n-2][arr[n-1]])