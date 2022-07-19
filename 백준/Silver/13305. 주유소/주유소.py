import sys
input = sys.stdin.readline
n=int(input())
km = list(map(int,input().split()))
money = list(map(int,input().split()))
res = km[0] * money[0]
m = money[0]
dist = 0
for i in range(1, n-1):
  if money[i] < m: #기존 금액보다 적으면
    res += m*dist #최소 금액만 더함
    dist = km[i] #다음 거리
    m = money[i]
  else: #기존 금액보다 크면
    dist += km[i] #계산해야 할 거리만 더 늘려줌
  if i == n-2: #마지막 구간이면
    res += m*dist
print(res)