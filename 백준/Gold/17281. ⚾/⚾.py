import sys
from itertools import permutations as pt
input = sys.stdin.readline
n = int(input())
inning = [list(map(int,input().split())) for _ in range(n)]
answer = 0

def play(arr):
    tmp = 0
    score = 0
    for inn in inning:
        out = 0 # 아웃
        one, two, three = 0, 0, 0 # 1루, 2루, 3루
        # 3아웃 전까지 계속 점수 획득
        while out < 3:
            hit = inn[arr[tmp]]
            if hit == 0: # 아웃
                out += 1
            elif hit == 1: # 1루
                score += three
                one, two, three = 1, one, two
            elif hit == 2: # 2루
                score += (two + three)
                one, two, three = 0, 1, one
            elif hit == 3:
                score += (one + two + three)
                one, two, three = 0, 0, 1
            elif hit == 4:
                score += (1 + one + two + three)
                one, two, three = 0, 0, 0
            tmp = (tmp + 1) % 9
    return score

for i in pt(range(1,9), 8):
    baseball = list(i[:3]) + [0] + list(i[3:]) # 4번 타자 고정
    answer = max(answer, play(baseball))
print(answer)