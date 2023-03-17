T, W = map(int,input().split())
dp = [[0 for _ in range(W+2)] for _ in range(T)]
for i in range(T):
    tree = int(input()) - 1 # 0 or 1
    for j in range(1, W+2): # 이동횟수 1(0), 2(1), 3(2)
        if j % 2 != tree: # 나무 0번 == 이동횟수 1(0), 3(2), 5(4), ... : 자두 획득
            tmp = 1
        else:
            tmp = 0
        dp[i][j] = max(dp[i-1][j] + tmp, dp[i-1][j-1] + tmp)
print(max(dp[-1]))