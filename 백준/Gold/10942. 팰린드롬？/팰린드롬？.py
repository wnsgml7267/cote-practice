import sys
input =sys.stdin.readline
N = int(input())
arr =  list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for left in range(N):
        right = left + i
        
        if right >= N:
            break
            
        if left == right:
            dp[left][right] = 1

        elif left + 1 == right:
            if arr[left] == arr[right]:
                dp[left][right] = 1
        elif arr[left] == arr[right] and dp[left+1][right-1]:
            dp[left][right] = 1
for i in range(int(input())):
    x, y = map(int, input().split())
    print(dp[x-1][y-1])
