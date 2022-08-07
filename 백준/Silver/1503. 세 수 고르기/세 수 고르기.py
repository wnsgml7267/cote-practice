N, M =map(int,input().split()) #자연수, 집합의 크기
#집합의 크기 0인 경우
answer=10**9
arr = [True for _ in range(1002)]
if M == 0:
  print(0)
else:
  s = list(map(int,input().split())) #집합 S에 들어있는 수
  for i in range(1,1001):
    if i not in s:
      start = i #첫 최소 x 값
      break
  for i in s:
    arr[i] = False
      
  if start >= 10:
    answer = abs(N-start**3)
  else:
    for k in range(start, 10):
      if arr[k] == False:
        continue
      for i in range(start, 33):
        if arr[i] == False:
          continue
        for j in range(start,1002):
          if arr[j] == False:
            continue
          answer = min(answer, abs(N-k*i*j))
  print(answer)