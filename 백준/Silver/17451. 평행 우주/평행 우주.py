import sys
input = sys.stdin.readline
n= int(input())
speed = list(map(int,input().split()))
ans = 0
for i in range(n-1,-1,-1):
  if ans <= speed[i]:
    ans = speed[i]
  else:
    if ans % speed[i]:
      ans = (ans // speed[i] + 1) * speed[i]
print(ans)
    