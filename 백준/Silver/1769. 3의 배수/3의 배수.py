import sys
input = sys.stdin.readline
a=input().rstrip()
count = 0
result = 0
def change(x):
  global count
  if len(x) == 1:
    print(count)
  else:
    re = 0
    for i in x:
      re += int(i)
    count += 1
    change(str(re))
change(a)
if int(a) % 3 == 0:
    print("YES")
else:
    print("NO")