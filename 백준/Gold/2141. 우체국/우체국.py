import sys
input = sys.stdin.readline
import math
n=int(input())
city = []
total = 0
cnt = 0
for i in range(n):
  position, people = map(int,input().split()) #위치, 거주하는 사람
  city.append([position,people])
  total += people #총 인원
city.sort()
for i in range(n):
  cnt += city[i][1]
  if cnt >= math.ceil(total/2): #누적된 인구수가 중간값과 같거나 넘어가는 순간
    print(city[i][0])
    break