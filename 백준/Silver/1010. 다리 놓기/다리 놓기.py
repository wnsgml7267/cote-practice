for _ in range(int(input())):
  n, m = map(int,input().split())
  if n == m:
    print(1)
  else:
    answer = 1
    for i in range(n):
      a = (m-n+(i+1))
      answer *= a
    for j in range(n, 1, -1):
      answer = answer // j
    print(answer)
    