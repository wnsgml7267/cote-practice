a=[]
b=[]
for i in range(3):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
for i in a:
    if a.count(i) == 1:
        x1=i
for j in b:
    if b.count(j) == 1:
        y1=j
print(x1,y1)
