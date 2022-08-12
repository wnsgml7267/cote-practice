s=list(input())
visit = 0
temp = 0
for i in range(len(s)):
  if s[i] == '<':
    s[temp:i] = (s[temp:i])[::-1]
    visit = 1
  elif s[i] == '>':
    visit = 0
    temp = i+1
    continue
  if visit == 0:#부등호 밖이면
    if s[i] == " ":
      s[temp:i] = (s[temp:i])[::-1]
      temp = i+1
    if i == len(s)-1: #마지막에 도달하면
      s[temp:i+1] = (s[temp:i+1])[::-1]
for i in s:
  print(i,end="")
    
    
    
  