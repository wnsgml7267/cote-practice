# N까지 소수들의 합을 구해서 누적합이 N이 되는지 확인
import math, sys
input = sys.stdin.readline
N = int(input())
visited = [False, False] + [True]*(N-1) #모든 수가 소수인 것으로 초기화
array = [] #누적합 저장
cnt = 0 # 횟수

for i in range(2, int(math.sqrt(N)) + 1):
    if visited[i] == True: #i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= N:
            visited[i*j] = False
            j += 1

for i in range(2, N+1):
    if visited[i]:
        array.append(i) #누적합

left, right = 0, len(array)-1

while left <= right:
    h = 0
    for i in range(left, right+1):
        h += array[i]
        if h == N:
            cnt += 1
            left += 1
            break
        elif h > N:
            left += 1
            break
        if left == right:
            left += 1
            break
print(cnt)