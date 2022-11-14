n, s = map(int,input().split()) #길이, 합
arr = list(map(int,input().split()))
left, right = 0, 0
ans = 100001
add = arr[0] #연속된 누적합

while True:
    if add >= s: #누적합이 원하는 값(s) 이상이면
        add -= arr[left]
        ans = min(ans, right - left + 1) #최소 길이
        left += 1
    else:
        right += 1
        if right == n: #끝 지점까지 도달 시 break
            break
        add += arr[right]

if ans == 100001:
    print(0)
else:
    print(ans)
