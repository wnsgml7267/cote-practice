from collections import deque
n=int(input())
s=input()
dic = dict()
chrA = 65
for i in range(chrA, chrA+n):
  dic[chr(i)] = int(input())
s=list(s)
for i in range(len(s)):
  if s[i] in dic.keys():
    s[i] = dic.get(s[i])
s = deque(s)
sss=['*','/','+','-']
answer = []
while s:
  ss = s.popleft()
  if ss in sss:
    if ss == '*':
      q = answer.pop()
      w = answer.pop()
      answer.append(q*w)
    elif ss == '/':
      q = answer.pop()
      w = answer.pop()
      answer.append(w/q)
    elif ss == '+':
      q = answer.pop()
      w = answer.pop()
      answer.append(q+w)
    elif ss == '-':
      q = answer.pop()
      w = answer.pop()
      answer.append(w-q)
  else:
    answer.append(ss)
print(format(answer[0],".2f"))
#chr65~90 A~Z 아스키코드를 문자열로