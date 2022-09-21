import sys
input = sys.stdin.readline
a, b = map(int,input().split())
cnt = 0
while a<b:
    if str(b)[-1] == '1':
      b = int(str(b)[:-1])
      cnt += 1
    else:
      if b%2 != 0:
        b = a-1
      else:
        b = b//2
        cnt += 1
        
if a == b:
    print(cnt+1)
else:
    print(-1)
    