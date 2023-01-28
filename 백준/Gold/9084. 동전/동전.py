"""
주어진 금액을 만드는 모든 방법

1~20가지 동전
각 금액은 1~10000원
만들어야 할 금액 1~10000원

2 3 5 (오름차순) / 만들어야 할 금액 10

  0 1 2 3 4 5 6 7 8 9 10
2 1 0 1 0 1 0 1 0 1 0 1
3 1 0 1 1 1 1 2 1 2 2 2
5 1 0 1 2 1 2 2 2 3 3 4
"""

t = int(input()) # 테스트 케이스
for _ in range(t):
    N = int(input()) # 동전 가지 수
    arr = list(map(int,input().split())) # 동전 리스트
    M = int(input()) # 목표 금액

    dp = [0 for _ in range(M+1)] # 각 인덱스 == 목표 금액 도달 경우의 수
    dp[0] = 1 # 목표 금액과 동전 금액(coin)이 같은 경우 1가지 추가

    for coin in arr:
        for target in range(1,M+1):
            if target >= coin:
                dp[target] += dp[target - coin]
    print(dp[M])

