n=int(input())
dp = [ 1 for _ in range(n)]
line = []
for i in range(n):
  #왼쪽 전깃줄, 오른쪽 전깃줄  
  x, y = map(int,input().split())
  line.append([x,y])
#왼쪽 전깃줄 오름차순 기준으로 정렬
line.sort(key = lambda x:x[0])
#오른쪽 전깃줄
right_line = []
for i2 in range(n):
  right_line.append(line[i2][1])
#가장 긴 증가하는 부분수열 구하기
for j in range(n):
  for k in range(j):
    if right_line[j] > right_line[k]:
      dp[j] = max(dp[j], dp[k]+1)
print(n-max(dp))
  