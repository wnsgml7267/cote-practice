import sys
input = sys.stdin.readline
n = int(input())
dp = [1]*n
lst = []
lst = [sorted(list(map(int,input().split()))) for i in range(n)]
lst.sort()
for i in range(n):
  for j in range(i):
    if lst[i][1] >= lst[j][1]:
      dp[i] = max(dp[i],dp[j]+1)
print(max(dp))