from math import floor
x, y = map(int, input().split())
percent = floor(100 * y / x) # 부동소수점 오차
low, high = 0, 10**9
if percent >= 99: # 확률이 99~100퍼면
    print(-1)
else:
    while low <= high: # 이분 탐색
        mid = (low + high) // 2
        tx, ty = x + mid, y + mid
        change_percent = floor(100 * ty / tx)
        if  change_percent > percent: 
            high = mid - 1
        else: 
            low = mid + 1
    print(high + 1)