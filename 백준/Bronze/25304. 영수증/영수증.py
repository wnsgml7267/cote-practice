x=int(input())
q=0
for i in range(int(input())):
  a,b=map(int,input().split())
  q+=a*b
if q==x: print("Yes") 
else: print("No")