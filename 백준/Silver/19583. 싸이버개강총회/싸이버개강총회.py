import sys
input = sys.stdin.readline
s,e,q = input().split() #시작 시간, 끝낸 시간, 스트리밍 끝낸 시간
s = int(s[:2])*60+int(s[-2:])
e = int(e[:2])*60+int(e[-2:])
q = int(q[:2])*60+int(q[-2:])
#출석 : 시작 시간까지 + 끝낸 시간부터 스트리밍 끝낸 시간 까지 
from collections import defaultdict
cnt = 0
dict = defaultdict(list)
for line in sys.stdin.readlines():
  time, student = line.split()
  dict[student].append(time)

for i in dict: #키(student) 값 꺼냄
  tmp = 0
  for j in dict[i]:
    chat = int(j[:2])*60+int(j[-2:]) #채팅 기록 시간
    if s >= chat: #시작 시간 전에 채팅
      tmp += 1
    elif e <= chat <= q:
      if tmp != 0:
        cnt += 1
        break
print(cnt)
    
