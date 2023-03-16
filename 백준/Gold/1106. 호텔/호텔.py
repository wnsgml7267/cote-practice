necessary_customer_cnt, city_cnt = map(int,input().split()) # 필요한 고객 수, 도시 수
city_arr = [list(map(int,input().split())) for _ in range(city_cnt)] # 인덱스 0 : 비용, 인덱스 1 : 고객
dp = [10**9] * (necessary_customer_cnt + 100)
dp[0] = 0
for i in range(necessary_customer_cnt + 100):
    for cost, man in city_arr:
        dp[i] = min(dp[i-man] + cost, dp[i])
print(min(dp[necessary_customer_cnt:]))