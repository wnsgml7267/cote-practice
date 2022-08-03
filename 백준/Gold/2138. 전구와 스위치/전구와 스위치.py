n = int(input())
c = list(map(int,input().rstrip("\n")))
want = list(map(int,input().rstrip("\n")))

def change(num):
  if num == 0:
    num = 1
  else:
    num = 0
  return num

def switch(c, cnt):
  count = cnt
  if count == 1:
    c[0] = change(c[0])
    c[1] = change(c[1])
  for i in range(1,n):
    if c[i-1] != want[i-1]:
      count += 1
      c[i-1] = change(c[i-1])
      c[i] = change(c[i])
      if i != n-1:
        c[i+1] = change(c[i+1])
  if c == want:
    return count
  else:
    return -1
res1 = switch(c[:],0)
res2 = switch(c[:],1)
if res1 >= 0 and res2 >= 0:
  print(min(res1, res2))
elif res1 >=0 and res2 < 0:
  print(res1)
elif res1 <0 and res2 >= 0:
  print(res2)
else:
  print(-1)