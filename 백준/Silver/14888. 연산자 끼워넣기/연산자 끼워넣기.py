n = int(input())
arr = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
mx, mn = -1e9, 1e9

def back(idx, val, add, sub, mul, div):
    global mx, mn
    if idx == n: 
        mx, mn = max(mx, val), min(mn, val) 
        return
    if add > 0: back(idx+1, val+arr[idx], add-1,sub,mul,div)
    if sub > 0: back(idx+1, val-arr[idx],add,sub-1,mul,div)
    if mul > 0: back(idx+1, val*arr[idx],add,sub,mul-1,div)
    if div > 0: back(idx+1, int(val/arr[idx]),add,sub,mul,div-1)
        
back(1,arr[0],a,b,c,d)

print(mx)
print(mn)