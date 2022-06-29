import sys
input = sys.stdin.readline
n = int(input())
snow = sorted(list(map(int,input().split())))
ans = 10**9+1

for i in range(n):
  for j in range(i+3,n):
    left, right = i+1, j-1
    while left < right:
      r = (snow[i]+snow[j]) - (snow[left]+snow[right])
      ans = min(abs(ans), abs(r))
      if r < 0:
        right -= 1
      else:
        left += 1
print(ans)