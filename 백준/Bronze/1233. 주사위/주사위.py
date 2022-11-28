from collections import Counter
n, m, l = map(int,input().split())
c = Counter()
mx = 0
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(1, l+1):
            c[i+j+k] += 1
for i in c.keys():
    if c[i] > mx:
        mx = c[i]
        ans = i
print(ans)