from collections import defaultdict as dd
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
dp = [1 for _ in range(n)]

dic = dd(int)
dic[arr[0]] = 1
for i in range(1, n):
  dic[arr[i]] = 1
  if dic[arr[i]-1]: # 연속된 번호라면
    dic[arr[i]] = dic[arr[i]-1] + 1
print(n - max(dic.values()))