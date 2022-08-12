s=list(input())
copy = s
visit = 0
temp = 0
for i in range(len(s)):
  if s[i] == '<':
    a = s[temp:i]
    copy[temp:i] = a[::-1]
    visit = 1
  elif s[i] == '>':
    visit = 0
    temp = i+1
    continue
  if visit == 0:#부등호 밖이면
    if s[i] == " ":
      a = s[temp:i]
      copy[temp:i] = a[::-1]
      temp = i+1
    if i == len(s)-1: #마지막에 도달하면
      a = s[temp:i+1]
      copy[temp:i+1] = a[::-1]
for i in copy:
  print(i,end="")
    
    
    
  