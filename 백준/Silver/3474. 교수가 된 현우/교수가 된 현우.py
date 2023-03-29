import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
  n = int(input())
  five = 5
  cnt = 0
  while(n >= five):
    cnt += n // five
    five *= 5
  print(cnt)