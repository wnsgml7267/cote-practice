n,m=map(int,input().split())
a = list(map(int,input().split()))
ans = True
wm = 0
for i in range(n-1,0,-1):
  wm += a[i]
  if a[i-1]-m < wm/(n-i) < a[i-1]+m:
    ans = True
  else:
    ans = False
    break
print('stable') if ans==True else print('unstable')
