import sys
input = sys.stdin.readline
m = int(input())
s = set()
for i in range(m):
  a = input().split()
  if len(a) == 1:
    if a[0] == "all":
      s = set([i for i in range(1,21)])
    else:
      s = set()
  else:
    x,y = a[0], int(a[1])
    if x == "add":
      s.add(y)
    elif x == "remove":
      s.discard(y)
    elif x == "check":
      if y in s:
        print(1)
      else:
        print(0)
    elif x == "toggle":
      if y in s:
        s.discard(y)
      else:
        s.add(y)
      