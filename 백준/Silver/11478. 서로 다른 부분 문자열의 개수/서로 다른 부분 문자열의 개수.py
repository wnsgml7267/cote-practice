s = input()
answer = []
count = 0
for i in range(1,len(s)+1):
  for j in range(len(s)):
    if j+i <= len(s):
      answer.append(s[j:j+i])
print(len(set(answer)))