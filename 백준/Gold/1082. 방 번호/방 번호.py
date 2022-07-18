import sys
input = sys.stdin.readline
N=int(input()) #0~N-1방 번호
P=list(map(int,input().split())) #방마다 가격
M=int(input()) #가진 돈
dp = [-float("inf") for _ in range(M+1)] #가격 dp
for i in range(N-1,-1,-1): #내림차순하여, 제일 큰 수 부터 구매하는데, 길이가 제일 길어야함.
  p = P[i] #해당 번호의 가격
  for j in range(p, M+1): #해당 번호의 가격 ~ 가진 돈
    dp[j] = max(dp[j], i, dp[j-p]*10+i) #max(현재 값, 현재 인덱스 값, 이전 값*10+현재 값)
print(dp[M])

