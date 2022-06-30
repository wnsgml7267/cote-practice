import sys
input = sys.stdin.readline

n,r,c=map(int,input().split())
ans = 0

def solve(x,y,n):
  global ans
  if x==r and y==c:
    print(ans)
    exit(0)
  if n==1:
    ans += 1
    return
  if not (x <= r < x+n and y <= c < y+n):
    ans += n*n
    return
  tmp = n//2
  solve(x,y,tmp)
  solve(x,y+tmp,tmp)
  solve(x+tmp,y,tmp)
  solve(x+tmp,y+tmp,tmp)
solve(0,0,2**n)
print(ans)