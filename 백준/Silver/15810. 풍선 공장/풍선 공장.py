import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 스태프의 수, 풍선의 개수

times = list(map(int,input().split()))

'''
- x초 일 때 몇 개가 만들어지는지 확인하기.
x의 최솟값 : 1
x의 최댓값 : 풍선의 개수(M) * 스태프가 풍선 하나를 만드는 최소 시간
'''

left, right = 1, m * max(times)

while left <= right:
    mid = (left + right) // 2

    cnt = 0 # 풍선의 개수 체크

    for time in times:
        cnt += mid // time # 풍선 만들기

    if cnt >= m: # 만든 풍선의 개수가 m개를 넘으면
        right = mid - 1
    else:
        left = mid + 1
print(left)
