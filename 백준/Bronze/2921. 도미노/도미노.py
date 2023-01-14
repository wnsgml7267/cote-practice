n = int(input())
cnt = 0
for i in range(1,n+1):
    for j in range(i+1):
        cnt += (i+j)
print(cnt)        