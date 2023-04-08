from collections import defaultdict as dd
n = int(input())
arr = list(map(int,input().split()))
dic = dd(int)
for i in range(n):
  t = arr[i] 
  dic[t] = dic[t-1] + 1
print(n - max(dic.values()))