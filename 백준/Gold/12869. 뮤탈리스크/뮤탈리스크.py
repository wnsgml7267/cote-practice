from itertools import permutations as pt

def per(x, y, z, cnt):

    global hp_max

    if x <= 0 and y <= 0 and z <= 0: # scv를 모두 처치했을 때
        hp_max = min(hp_max, cnt) # 처치한 최소 공격횟수 초기화
        return

    if x <= 0: x = 0
    if y <= 0: y = 0
    if z <= 0: z = 0

    # 이미 방문했고, 지금보다 최소 공격횟수인 scv 체력들이면 리턴
    if dp[x][y][z] <= cnt:
        return

    dp[x][y][z] = cnt

    # 순열 : 뮤탈이 할 수 있는 모든 공격 방법으로 scv 체력을 깎는다
    for i in pt([9,3,1], 3):
        per(x - i[0], y - i[1], z - i[2], cnt + 1)

N = int(input())
scv = list(map(int,input().split()))
while len(scv) < 3:
    scv += [0]
scv_max_hp = max(scv) # scv 중 최대 체력
hp_max = 61 # scv 체력이 될 수 없는 default 값
dp = [[[hp_max] * (scv_max_hp +1) for _ in range(scv_max_hp+1)] for _ in range(scv_max_hp+1)]
per(scv[0], scv[1], scv[2], 0)

print(hp_max)