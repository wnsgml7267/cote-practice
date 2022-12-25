n, k = map(int,input().split())
cnt = 0
bol = True
for i in range(1,n+1):
    if n % i == 0:
        cnt += 1
        if cnt == k:
            print(i)
            bol = False
            break
if bol:
    print(0)
        