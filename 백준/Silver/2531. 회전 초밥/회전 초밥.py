import sys
from collections import deque
input = sys.stdin.readline
n,d,k,c = map(int,input().split()) #접시 수, 가짓수, 연속접시수, 쿠폰번호
sushi = [] #초밥들
answer = []
for i in range(n):
  sushi.append(int(input()))
sushi = deque(sushi)
for i in range(n):
  sushi.rotate(-1) #왼쪽 회전
  su = list(sushi)[:k]
  su.append(c)
  answer.append(len(set(su)))
print(max(answer))

