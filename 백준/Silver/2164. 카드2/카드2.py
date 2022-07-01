from collections import deque
lst = deque()
N = int(input())
if N == 1:
  print(N)
elif N == 3:
  print(2)
elif N == 2:
  print(2)
else:
  #짝수일때46
  if N % 2 == 0:
    for i in range(4,N+1,2):
      lst.append(i)
  #홀수일때 246
  else:
    for j in range(2,N+1,2):
      lst.append(j)
  while(len(lst) != 1):
    lst.append(lst.popleft())
    lst.popleft()
  
  print(lst[0])