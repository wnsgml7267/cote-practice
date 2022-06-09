#물 새는 위치 개수, 테이프 길이
position_count, tape = map(int,input().split())
#물 새는 위치 리스트
position = list(map(int,input().split()))
position.sort()
#테이프 개수
tape_count = 0
#현재 위치
position_now = 0

for i in position:
    if position_now <= i:
        position_now = i + (tape-0.5)
        tape_count += 1
print(tape_count)

