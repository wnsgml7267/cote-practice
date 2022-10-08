import sys
input = sys.stdin.readline
n, k = map(int,input().split())
array = list(map(int,input().split()))

max_len = 0 #짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이를 출력한다.
for i in range(n):
    if array[i] % 2: #홀수면
        continue
    else: #짝수일 때만 시작
        long_len = 1 #부분 수열 길이
        hol_count = 0 #홀수 갯수
    for j in range(i+1, n):
        if hol_count > k:
            break
        if array[j] % 2: #홀수면
            hol_count += 1
        else:
            long_len += 1
    max_len = max(max_len, long_len)
print(max_len)
