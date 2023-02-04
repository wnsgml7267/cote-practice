n, m = map(int,input().split()) # 녹화 개수, 블루레이 개수
size = list(map(int,input().split())) # 녹화 길이

ans = 0 

left, right = max(size), sum(size)

while left <= right:
    mid = (left + right) // 2 # 블루레이 크기(녹화 시간)

    blue_count, recoding = 0, 0 # 블루레이 개수, 블루레이 크기(녹화 시간) 체크

    for i in range(n):
        if recoding + size[i] > mid: # 녹화 시간이 더 길면
            blue_count += 1 #블루레이 개수 증가
            recoding = 0
        recoding += size[i]

    if recoding > 0: # 녹화 시간이 남아 있으면 블루레이 1개 추가
        blue_count += 1

    if blue_count > m: # 블루레이 크기를 넘어섰다면 녹화시간을 더 길게
        left = mid + 1
    else:
        right = mid - 1
print(left)
        

    
