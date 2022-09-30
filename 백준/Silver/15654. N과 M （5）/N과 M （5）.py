from itertools import permutations as pt
n, m = map(int,input().split())
array = sorted(list(map(int,input().split())))
for i in list(pt(array, m)):
    print(*i)