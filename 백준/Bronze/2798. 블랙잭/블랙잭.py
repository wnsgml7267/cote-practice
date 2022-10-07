n,m=map(int , input().split())
array = list(map(int,input().split()))
answer = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            d = array[i]+array[j]+array[k]
            if d <= m:
                answer=max(answer,d)
print(answer)
            