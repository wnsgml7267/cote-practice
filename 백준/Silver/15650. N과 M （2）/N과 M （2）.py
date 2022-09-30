from itertools import combinations as cb
n, m = map(int,input().split())
array = [i for i in range(1,n+1)]
for i in list(cb(array, m)):
    print(*i)