def man(s):
  for i in range(s, len(switch)+1, s):
    change(i-1)
    
def girl(s):
  change(s-1)
  m = min(s,switch_count-s+1)
  if m != 1:
    for i in range(1,m):
      if switch[(s-1)-i] == switch[(s-1)+i]:
        change((s-1)-i)
        change((s-1)+i)
      else:
        break
      
def change(chg):
  if switch[chg] == 1:
    switch[chg] = 0
  else:
    switch[chg] = 1
    
switch_count = int(input())
switch = list(map(int,input().split()))
person = int(input())
for i in range(person):
  gender, num = map(int,input().split())
  if gender == 1:
    man(num)
  elif gender == 2:
    girl(num)
for j in range(switch_count):
  if j != 0 and j % 20 == 0:
    print()
  print(switch[j], end=' ')