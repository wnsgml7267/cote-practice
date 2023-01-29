x, y = map(int, input().split())
percent = y * 100 // x
low, high = 0, 10**9
answer = 0
while low <= high:
    mid = (low+high)//2
    if (y+mid) * 100 // (x+mid) > percent:
        high = mid - 1
        answer = mid
    else:
        low = mid + 1
if answer == 0:
    print(-1)        
else:
    print(answer)