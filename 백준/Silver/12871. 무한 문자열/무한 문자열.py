s = input()
t = input()
answer = 0
if len(s) < len(t):
  if s*len(t) == t*len(s):
    answer = 1
elif len(s) > len(t):
  if t*len(s) == s*len(t):
    answer = 1
else:
  if t == s:
    answer = 1
print(answer)