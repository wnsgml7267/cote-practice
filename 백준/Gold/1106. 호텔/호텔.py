customer_cnt, city_cnt = map(int,input().split()) # 필요한 고객 수, 도시 수

city_arr = []
for city in range(city_cnt):
    city_arr.append(list(map(int,input().split())))
city_arr.sort()

dp = [10**9] * (customer_cnt + 100) # 고객과 비용은 최대 100 이하
dp[0] = 0
for cost, man in city_arr:
    for i in range(man, customer_cnt + 100):
        dp[i] = min(dp[i-man] + cost, dp[i])
print(min(dp[customer_cnt:]))