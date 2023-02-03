import sys
input = sys.stdin.readline
n, k = map(int,input().split()) # 캐릭터의 개수, 올릴 수 있는 레벨 총합
levels = []
for _ in range(n):
    levels.append(int(input()))
left, right = min(levels), min(levels) + k

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for level in levels:
        if mid > level : cnt += mid - level

    if cnt > k:
        right = mid - 1
    else:
        left = mid + 1
print(right)