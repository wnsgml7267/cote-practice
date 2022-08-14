import sys
input = sys.stdin.readline
n = int(input())
ink = list(map(int,input().split()))
jum = list(map(int,input().split()))
ans = []
for i in range(len(ink)):
  tmp = ink[i] #잉크 저장
  start = 0
  end = n-1
  while start <= end:
    mid = (start + end)//2
    if jum[mid] > tmp:#점도가 잉크보다 크면
      end = mid-1
    else:
      start = mid+1
  ans.append(start-i-1)
print(*ans)