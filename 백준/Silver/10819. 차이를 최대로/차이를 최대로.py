from itertools import permutations as pt
n = int(input())
answer = 0
array = list(map(int,input().split()))
for i in list(pt(array, n)):
  cnt = 0
  for j in range(n-1):
    cnt += abs(i[j]-i[j+1])
  answer = max(answer, cnt)
print(answer)