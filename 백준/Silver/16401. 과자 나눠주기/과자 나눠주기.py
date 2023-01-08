import sys
input = sys.stdin.readline
m, n = map(int,input().split()) #조카의 수, 과자의 수
snack = list(map(int,input().split()))
start, end = 1, max(snack)
answer = 0
while start <= end:
  mid = (start+end)//2
  cnt = 0
  for i in snack:
    cnt += (i//mid)
  
  if cnt < m: #과자를 모두 분배했을 때 조카의 수보다 적으면
    end = mid - 1
  else:
    start = mid + 1
    answer = max(answer, mid)
print(answer)
