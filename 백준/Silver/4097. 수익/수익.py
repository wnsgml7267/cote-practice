import sys
input = sys.stdin.readline
while True:
  n = int(input())
  if n == 0:
    break
  dp = []
  for i in range(n):
    num = int(input())
    dp.append(num)
  for i in range(1,n):
    dp[i] = max(dp[i], dp[i]+dp[i-1])
  print(max(dp))
  
    
    