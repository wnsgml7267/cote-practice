from collections import deque
gear = []
cnt = 0

for _ in range(4):
    gear.append(deque(input()))

k = int(input()) # 회전 횟수

def left(number, dir): # 극, 번호, 방향
    if number < 1 or gear[number][6] == gear[number-1][2]:
        return
    if gear[number][6] != gear[number-1][2]:
        left(number-1, -dir)
        if dir == 1:
            gear[number-1].appendleft(gear[number-1].pop())
        elif dir == -1:
            gear[number-1].append(gear[number-1].popleft())

def right(number, dir):
    if number > 4 or gear[number-2][2] == gear[number-1][6]:
        return
    if gear[number-2][2] != gear[number-1][6]:
        right(number + 1, -dir)
        if dir == 1:
            gear[number-1].appendleft(gear[number-1].pop())
        elif dir == -1:
            gear[number-1].append(gear[number-1].popleft())

for _ in range(k):
    num, direction = map(int,input().split()) # 톱니바퀴 번호, 방향(1:시계,-1:반시계)

    left(num - 1, -direction)
    right(num + 1, -direction)

    if direction == 1:
        gear[num-1].appendleft(gear[num-1].pop())
    elif direction == -1:
        gear[num-1].append(gear[num-1].popleft())


if gear[0][0] == '1':
    cnt += 1
if gear[1][0] == '1':
    cnt += 2
if gear[2][0] == '1':
    cnt += 4
if gear[3][0] == '1':
    cnt += 8

print(cnt)