import sys
input = sys.stdin.readline

x, y, z = map(int,input().split())
vol = x * y * z # 전체 부피
n = int(input())

cube = [list(map(int,input().split())) for _ in range(n)]
cube.sort(reverse=True) # 제일 큰 정육면체부터

result = 0 # 필요 큐브 개수
total = 0 # 총 채운 부피

for idx, cnt in cube:
    total *= 8 # 이전 정육면체 부피의 1/8
    square = 2 ** idx # 2**i 정육면체

    # 현재 공간에 채울 수 있는 개수 - 지금까지 채운 개수
    fill = (x // square) * (y // square) * (z // square) - total
    fill = min(cnt, fill) # 실제로 채우기 가능한 개수

    result += fill
    total += fill

if total == vol:
    print(result)
else:
    print(-1)