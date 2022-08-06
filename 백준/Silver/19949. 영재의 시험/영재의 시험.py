answer = list(map(int,input().split()))
li, cnt = [], 0
def back(depth):
  global cnt
  if depth == 10:
    s = 0
    for j in range(10):
      if li[j] == answer[j]:
        s += 1
    if s >= 5:
      cnt += 1
    return ;
  for i in range(1,6): #5지 선다
    if depth > 1 and li[depth-2] == li[depth-1] == i: #연속된 3개의 값이 같은 경우는 제외
      continue
    li.append(i)
    back(depth+1)
    li.pop()
back(0)
print(cnt)