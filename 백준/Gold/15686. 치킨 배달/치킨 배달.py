from itertools import combinations
import sys
input = sys.stdin.readline
n,m=map(int,input().split()) #nxn / 최대 치킨집 수
graph = [list(map(int,input().split())) for i in range(n)]

answer = 999999
house = []
chic = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      house.append([i,j])
    elif graph[i][j] == 2:
      chic.append([i,j])
for chicken in combinations(chic,m):
  ans = 0
  for i in range(len(house)):
    ck_distance = 51 #집과 치킨집 거리
    for j in range(m):
      ck_distance = min(ck_distance, abs(house[i][0]-chicken[j][0]) + abs(house[i][1]-chicken[j][1]))
    ans += ck_distance
  answer = min(answer, ans)
print(answer)
    
