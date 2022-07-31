for i in range(int(input())): #testcase
  n, m =map(int,input().split()) #구매 갯수, 존재하는 로또 번호
  dp = [[0]*(m+1) for i in range(n+1)] #m이하의 n개의 경우의 수
  dp[0] = [1]*(m+1)
  for i in range(1,n+1):
    for j in range(1,m+1):
      dp[i][j] = dp[i][j-1] + dp[i-1][j//2]
  print(dp[n][m])