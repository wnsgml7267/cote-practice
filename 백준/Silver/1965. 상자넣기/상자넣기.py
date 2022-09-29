n = int(input())
array = list(map(int,input().split()))
dp = [1 for i in range(n)]
for i in range(1,n):
  for j in range(i):
    if array[i] > array[j]: #더 작은 박스면
      dp[i] = max(dp[j]+1, dp[i])
print(max(dp))