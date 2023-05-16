import sys
input = sys.stdin.readline
from collections import defaultdict as dd
n = int(input())
mos = dd(int)
for i in range(n):
    start, end = map(int,input().split())
    mos[start] += 1
    mos[end] -= 1

mos_max_cnt, mos_cnt = 0, 0 # 모기 최대 수, 모기 수
s, e = 0, 0 # 입장, 퇴장
flag = False
for i in sorted(mos.keys()):
    mos_cnt += mos[i]
    if mos_cnt > mos_max_cnt: # 입장한 모기 수가 현재까지 최대 모기 수 보다 많아지면
        mos_max_cnt = mos_cnt # 최대 모기 수 초기화
        s = i
        flag = True
    elif mos_cnt < mos_max_cnt and mos_cnt - mos[i] == mos_max_cnt and flag:
        e = i
        flag = False
print(mos_max_cnt)
print(s, e)