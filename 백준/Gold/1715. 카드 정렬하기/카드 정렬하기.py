from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  heappush(arr, int(input()))
new_arr = []
answer = 0
if n == 1:
  print(0)
else:
  while arr:
    if len(arr) > 1:
      num = heappop(arr) + heappop(arr)
      answer += num
      heappush(arr, num)
    else:
      break
  print(answer)