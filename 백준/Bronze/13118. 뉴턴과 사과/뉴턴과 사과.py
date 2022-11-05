arr = list(map(int,input().split()))
x,y,z = map(int,input().split())
ans = 0
for i in range(len(arr)):
    if arr[i] == x:
        ans = i+1
print(ans)