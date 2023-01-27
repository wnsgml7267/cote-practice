import sys
input = sys.stdin.readline
sum_arr = [0 for _ in range(1000001)] #누적합
dp = [1 for _ in range(1000001)] #dp 1

for i in range(2, 1000001):
    j = 1
    while i * j <= 1000000:
        # i의 배수는 약수로 i를 가지고 있으므로 해당 i의 배수 인덱스에 약수 i의 값을 더해줌.
        dp[i*j] += i 
        j += 1
for i in range(1, 1000001):
    sum_arr[i] = sum_arr[i-1] + dp[i]

t = int(input())
for _ in range(t):
    n = int(input())    
    print(sum_arr[n])