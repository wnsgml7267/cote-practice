while True:
  s = input()
  if s == '*':
    break
  ans = 0
  if len(s) > 2:
    for i in range(len(s)-1):
      pair=[]
      for j in range(len(s)-(i+1)):
        pair.append(s[j]+s[j+(i+1)])
      if len(pair) != len(set(pair)):
        ans = 1
        break
  if ans == 0:
    print(s + " is surprising.")
  else:
    print(s + " is NOT surprising.")
              