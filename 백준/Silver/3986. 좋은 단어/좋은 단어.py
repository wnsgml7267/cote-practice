n = int(input())
cnt = 0
for i in range(n):
  s = input()
  stack = []
  for j in range(len(s)):
    if not stack:
      stack.append(s[j])
    else:
      if stack[-1] == s[j]:
        stack.pop()
      else:
        stack.append(s[j])
  if not stack:
    cnt += 1
print(cnt)