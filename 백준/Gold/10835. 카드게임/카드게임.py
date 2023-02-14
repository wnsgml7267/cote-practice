n = int(input())

left = list(map(int,input().split()))
right = list(map(int,input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

'''
1. 왼쪽 카드 버리기
2. 양쪽 카드 버리기
3. 오른쪽 카드 버리기(오른쪽 번호가 작을 경우에만)
'''

for i in range(n-1, -1, -1):
  for j in range(n-1, -1, -1):
    if left[i] > right[j]: # 1, 2, 3 적용
      dp[i][j] = max(dp[i+1][j], dp[i+1][j+1], right[j]+ dp[i][j+1])
    else:
      dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
print(dp[0][0])