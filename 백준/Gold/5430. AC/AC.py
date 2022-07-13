from collections import deque
import sys
input = sys.stdin.readline
cnt = 0
for _ in range(int(input())): #테스트케이스 개수
  func = input() #실행할 함수
  n = int(input()) #배열길이
  array = input().rstrip()
  r_count = 0   
  if n == 0:
    array = deque()
  else:
    array = deque(array[1:-1].split(','))
  for i in range(len(func)):
    if len(array) == 0: #배열이 비어있을 경우
      if func[i] == "D":
        cnt += 1 #에러 표시
        break
      else:
        continue
    else:
      if func[i] == "R":
        r_count += 1
      elif func[i] == "D":
        if r_count % 2 == 0:
          array.popleft()
        else:
          array.pop()
          
  if cnt > 0:
    print("error")
    cnt=0
  else:
    if r_count % 2 == 0:
        print("[" + ",".join(array) + "]")
    else:
        array.reverse()
        print("[" + ",".join(array) + "]")
    