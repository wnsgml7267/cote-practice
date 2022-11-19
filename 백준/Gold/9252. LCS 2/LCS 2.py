import sys
input = sys.stdin.readline
first = [0] + list(input().rstrip())
second = [0] + list(input().rstrip())
fl = len(first)
sl = len(second)
dp = [[""] * sl for _ in range(fl)]
for i in range(1,fl):
    for j in range(1,sl):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + first[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
print(len(dp[fl-1][sl-1]))                
print(dp[fl-1][sl-1])