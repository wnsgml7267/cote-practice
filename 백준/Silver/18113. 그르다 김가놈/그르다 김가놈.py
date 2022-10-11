import sys
input = sys.stdin.readline
N, K, M = map(int, input().split()) #김밥의 개수, 꼬다리의 길이, 김밥조각의 최소개수
L = []
for _ in range(N):
    kim = int(input().rstrip())
    if kim > K*2:
        L.append(kim-(2*K))
    elif kim - K > 0 and kim < 2 * K:
        L.append(kim-K)

if len(L) == 0:
    print(-1)
    exit(0)

P = -1
l,r = 1,max(L)

while l <= r:

    m = (l+r)//2 #조각 김밥의 최대 길이
    total = sum([i//m for i in L])

    if total < M:
        r = m-1
    else:
        l = m+1
        P = m

print(P)