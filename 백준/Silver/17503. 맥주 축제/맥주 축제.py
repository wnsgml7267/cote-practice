import sys
from heapq import heappop, heappush
input = sys.stdin.readline
'''
if 맥주의 도수 레벨 > 간 레벨 : 사망
하루에 한 병 마실 수 있음. but 맥주 종류의 수는 축제 기간의 이상을 보유

선호도의 합 이상을 채우면서 간 레벨이 최소가 되는 경우. 
(그런 경우가 없으면 -1 => 맥주를 다 먹었는데 선호도를 못 채웠을 경우) 
'''
n, m, k = map(int,input().split()) # 축제 기간, 채워야 할 선호도의 합,  맥주 종류의 수

beers = []
for i in range(k):
    v, c = map(int,input().split()) # 맥주 선호도, 도수 레벨
    beers.append([v,c])
beers = sorted(beers, key = lambda x : (x[1], x[0]))

heap = []
f = 0
cnt = 0
left = 0
for beer in beers:
    f += beer[0]
    heappush(heap,beer[0])
    if len(heap) == n:
        if f >= m:
            answer = beer[1]
            break
        else:
            f -= heappop(heap)
else:
    print(-1)
    exit()
print(answer)


#선호도의 합이 넘으면

# 만약 먹은 맥주들의 도수들의 합이 간 레벨보다 높으면 사망하기 때문에 간 레벨을 높여줌??