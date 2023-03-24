import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify
t = int(input())
for i in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  heapify(arr)
  answer = 0
  while arr:
    if len(arr) > 1:
      num = heappop(arr) + heappop(arr)
      answer += num
      heappush(arr, num)
    else:
      break
  print(answer)