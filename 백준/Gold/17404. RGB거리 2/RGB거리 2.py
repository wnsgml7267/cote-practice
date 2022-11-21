n = int(input())
color = []
answer = 1000000
for i in range(n):
    red, green, blue = map(int,input().split())
    color.append([red, green, blue])
for i in range(3):
    dp = [[1000000, 1000000, 1000000] for _ in range(n)]
    dp[0][i] = color[0][i]
    for j in range(1,n):
        dp[j][0] = color[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = color[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = color[j][2] + min(dp[j-1][0], dp[j-1][1])
    for k in range(3):
        if i != k: #1번과 N번의 색상이 다를 경우만
            answer = min(answer, dp[-1][k])
print(answer)