import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
t=0
for k in range(n):
  t+=a[k]
  a[k]=t
for m in range(int(input())):
  i,j=map(int,input().split())
  if i==1:
    print(a[j-1])
  else:
    print(a[j-1]-a[i-2])