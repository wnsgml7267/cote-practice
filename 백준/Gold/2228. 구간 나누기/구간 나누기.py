import sys
input = sys.stdin.readline

n, m = map(int,input().split())

# [n+1][m+1]
contain = [[0] + [-1e9] * m for _ in range(n+1)] # i번째 수를 포함하는 j개 구간합
not_contain = [[0] + [-1e9] * m for _ in range(n+1)] # i번째 수를 포함하지 않는 j개 구간합

for i in range(1, n+1):
    section = int(input())
    for j in range(1, min(m, (i+1)//2)+1):
        # i-1번째까지 포함하지 않는 j개 구간합 최댓값
        not_contain[i][j] = max(contain[i-1][j], not_contain[i-1][j])
        # i-1번째까지 포함하는 j개 구간합 최댓값
        contain[i][j] = max(contain[i-1][j], not_contain[i-1][j-1]) + section
print(max(contain[n][m], not_contain[n][m]))