a = [0]
n = int(input())
for _ in range(n):
  a.append(int(input()))
if n == 1:
  print(a[1])
else:
  dp = [0] * (n+1)
  dp[1] = a[1]
  dp[2] = a[1]+a[2]
  for i in range(3, n+1):
    dp[i] = max(dp[i-3]+a[i-1]+a[i], dp[i-2]+a[i])
  print(dp[n])
