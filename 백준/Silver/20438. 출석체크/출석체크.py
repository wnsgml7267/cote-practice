import sys
input = sys.stdin.readline
n, k, q, m = map(int,input().split())
sleep = [0 for _ in range(n+3)]
check = [0 for _ in range(n+3)]

for i in map(int,input().split()):
  sleep[i] = 1
for i in map(int,input().split()):
  #출석코드 받은 사람이 자면 스킵
  if sleep[i]:
    continue
  for j in range(i, n+3, i):
    if not sleep[j]:
      #출석체크
      check[j] = 1
pre = [check[0]]
for i in range(1, n+3):
  pre.append(pre[-1]+check[i])

for _ in range(m):
  start, end = map(int,input().split())
  print(end - start + 1 - (pre[end] - pre[start - 1]))
