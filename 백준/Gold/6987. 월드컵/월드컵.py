import sys
input = sys.stdin.readline
from itertools import combinations as cb

def solution(round):
  global ans
  if round == 15:
    ans = 1
    for sub in res:
      #승,무,패의 값이 남아있으면 불가능
      if sub.count(0) != 3:
        ans = 0
        break
    return
  t1, t2 = game[round]
  #승패, 무무, 패승 비교
  for x,y in ((0,2), (1,1),(2,0)):
    if res[t1][x] > 0 and res[t2][y] > 0:
      res[t1][x] -= 1
      res[t2][y] -= 1
      solution(round + 1)
      res[t1][x] += 1
      res[t2][y] += 1
answer = []
#모든 경기 조합
game = list(cb(range(6),2))
#백트래킹
for _ in range(4):
  data = list(map(int,input().split()))
  res = [data[i:i+3] for i in range(0,16,3)]
  ans = 0
  solution(0)
  answer.append(ans)
print(*answer)