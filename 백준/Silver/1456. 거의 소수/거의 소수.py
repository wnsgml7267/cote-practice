import sys
input = sys.stdin.readline
start, end = map(int,input().split())
n = int(end**0.5)
state = [True] * (n+1)
state[1] = False
for i in range(2, n+1):
  if i*i > n:
    break
  if not state[i]:
    continue
  for j in range(i*i, n+1, i):
    state[j] = False
cnt = 0
for i in range(1, n+1):
  if state[i]:
    j = i*i
    while True:
      if j < start:
        j *= i
        continue
      if j > end:
        break
      j *= i
      cnt += 1
print(cnt)
  