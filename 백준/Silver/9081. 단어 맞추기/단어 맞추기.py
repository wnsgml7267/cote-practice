import sys
input = sys.stdin.readline

def next_per(s):
  k = -1
  for i in range(len(s)-1):
    if s[i] < s[i+1]:
      k=i
  if k == -1:
    return False
  for i in range(len(s)-1,-1,-1):
    if s[k] < s[i]:
      m=i
      break
  s[k], s[m] = s[m], s[k]
  l = s[:k+1]
  l.extend(list(reversed(s[k+1:])))
  return l
for _ in range(int(input())):
  str = input().rstrip()
  ans = next_per(list(str))
  if ans:
    print(''.join(ans))
  else:
    print(str)
  