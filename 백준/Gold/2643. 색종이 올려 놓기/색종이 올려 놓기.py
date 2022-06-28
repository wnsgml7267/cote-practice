import sys
input = sys.stdin.readline
n = int(input())
dp = [1]*n
lst = []
for i in range(n):
  x,y=map(int,input().split())
  if x > y:
    lst.append([y,x])
  else:
    lst.append([x,y])
lst.sort()
for i in range(n):
  for j in range(i):
    if lst[i][1] >= lst[j][1]:
      dp[i] = max(dp[i],dp[j]+1)
print(max(dp))