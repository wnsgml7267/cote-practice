import sys
input = sys.stdin.readline

n, k = map(int,input().split())
array = list(map(int, input().split()))

cnt = 0
start, end = 0, 0
size, size_max = 0, 0
flag = 1

for i in range(n):
    while cnt <= k and flag: #k만큼 삭제하기
        if array[end] % 2: #홀수면
            if cnt == k: #k만큼 삭제할 홀수가 나오면 break
                break
            cnt += 1 #홀수 개수 +1
        size += 1 #부분 수열의 길이
        if end == n - 1: #끝까지 돌면
            flag = 0 # 중지
            break
        end += 1
    size_max = max(size_max, size-cnt)
    if array[i] % 2:
        cnt -= 1
    size -= 1
print(size_max)
        
