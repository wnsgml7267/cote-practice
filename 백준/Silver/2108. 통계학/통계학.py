import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
num = []
for i in range(n):
  num.append(int(input()))
num.sort()

avg = sum(num)/n
mid = num[n//2]
#many_items = 
many = Counter(num).most_common(n=2)
rng = max(num) - min(num)
print(round(avg))#산술평균
print(mid)#중앙값
if len(many) > 1:
  if many[0][1] == many[1][1]:
    print(many[1][0])#최빈값
  else:
    print(many[0][0])
else:
  print(many[0][0])#최빈값
print(rng)#범위
