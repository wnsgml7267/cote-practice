bill = int(input()) # 지폐 금액
n = int(input())
dp = [1] + [0] * (bill)
for i in range(n):
    coin, cnt = map(int,input().split()) # 동전, 개수
    for b in range(bill, 0, -1):
        for count in range(1, cnt+1): # 해당 동전 개수 만큼
            if b-coin*count >= 0:
                dp[b] += dp[b-coin * count]
print(dp[bill])