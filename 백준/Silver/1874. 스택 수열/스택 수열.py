n=int(input())
array = []
answer = [] #+,-
equal = [] #동일 값
imp = [] #임시 
a=0
for i in range(n):
  array.append(int(input())) #만들어야 할 수열
start = [i for i in range(n,0,-1)] #n~1
for i in range(n):
  a=0
  while len(imp) >0:
    if imp[-1] == array[i]:
      imp.pop()
      answer.append('-')
      equal.append(array[i])   
      a=1
    else:
      break    
  while len(start) > 0:
    if a == 1:
      break
    po = start.pop() # 가져옴    
    if po == array[i]: #수열 값과 값이 같다면
      answer.append('+')
      answer.append('-')
      equal.append(po)
      break #해당 수열의 위치종료
    elif po < array[i]: #
      answer.append('+') #꺼내옴
      imp.append(po)                
      continue #해당 수열의 위치 계속
    elif po > array[i]:
      print("NO")
      exit(0)
if len(equal) == n:
  for i in answer:
    print(i)
else:
  print("NO")