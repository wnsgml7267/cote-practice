from sys import stdin
input = stdin.readline
#스택1
s = list(input().strip())
#스택2
s2 = []
#명령어 수행 횟수
count = int(input())
for i in range(count):
  #명령어
  cmd = input().strip()
  if cmd[0] == 'P' : 
    s.append(cmd[-1])
  elif cmd == 'L' and s != []:
    s2.append(s.pop())
  elif cmd == 'D' and s2 != []:
    s.append(s2.pop())
  elif cmd == 'B' and s != []:
    s.pop()
print("".join(s + list(reversed(s2))))
  
