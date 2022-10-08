from itertools import combinations as cb
n, k = map(int,input().split())
a = []
for i in range(1,n+1):
    a.append(i)
print(len(list(cb(a, k))))
