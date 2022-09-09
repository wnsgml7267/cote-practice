N, M = map(int,input().split())
array = list(map(int,input().split()))
left,right = 0,1
cnt = 0
while right <= N and left <= right:
    sum_array = array[left:right]
    answer = sum(sum_array)
    if answer == M:
        cnt += 1
        right += 1
    elif answer < M:
        right += 1
    else:
        left += 1
print(cnt)