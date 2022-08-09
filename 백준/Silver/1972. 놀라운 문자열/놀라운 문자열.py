while True:
  pair = []
  s = input()
  if s == '*':
    break
  ans = 0
  if len(s) == 2:
    if s[0] != s[1]:
      ans = 0
  elif len(s) == 1:
    ans = 0
  else:
    for i in range(len(s)-1):
      for j in range(len(s)-(i+1)):
        pair.append(s[j]+s[j+(i+1)])
      if len(pair) != len(set(pair)):
        ans = 1
        break
      else:
        pair=[]
        continue
  if ans == 0:
    print(s + " is surprising.")
  else:
    print(s + " is NOT surprising.")
              