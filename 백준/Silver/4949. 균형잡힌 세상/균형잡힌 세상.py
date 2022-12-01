while True:
  s = input()
  if s == '.':
    break
  arr = []
  flag = 0
  for i in s:
    if i == '[' or i == '(':
      arr.append(i)
    elif i == ']':
      if len(arr) == 0 or arr[-1] != '[':
        flag = 1
        break
      elif arr[-1] == '[':
        arr.pop()
    elif i == ')':
      if len(arr) == 0 or arr[-1] != '(':
        flag = 1
        break
      elif arr[-1] == '(':
        arr.pop()
  if flag == 0 and not arr:
    print('yes')
  else:
    print('no')
