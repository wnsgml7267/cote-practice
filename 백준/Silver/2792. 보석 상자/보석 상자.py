import sys, math # 빠른 입력, 올림(ceil) 사용을 위한 라이브러리 호출
input = sys.stdin.readline # 빠른 입력

jewel = [] # 보석들
jealousy = 1e9 # 질투심의 최솟값
n, m = map(int,input().split()) # 학생 수, 보석의 수
for _ in range(m): # 같은 색상의 보석 개수
    jewel.append(int(input()))

start, end = 1, max(jewel) # 받을 수 있는 질투심의 최솟값과 최댓값

while start <= end: # 이분 탐색

    mid = (start + end) // 2 # 중간 값(질투심)
    div = 0 # 현재 질투심으로 구한 학생 수

    for color in jewel: # 같은 색상 보석들 가져오기
        div += math.ceil(color/mid) # 학생 수 구하기
    
    if div > n: # 학생 수가 필요한 학생 수보다 더 많아진다면 
        start = mid + 1 # 질투심 증가
    else:
        end = mid - 1 # 질투심 감소
print(start)