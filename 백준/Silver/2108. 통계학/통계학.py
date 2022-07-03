import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
num = []
for i in range(n):
  num.append(int(input()))
num.sort()
many = Counter(num).most_common(n=2)
if len(many) > 1:
  if many[0][1] == many[1][1]:
    m = many[1][0]#최빈값
  else:
    m = many[0][0]
else:
  m = many[0][0]#최빈값
ans = [round(sum(num)/n), num[n//2], m, max(num) - min(num)]
for i in ans:
  print(i)
