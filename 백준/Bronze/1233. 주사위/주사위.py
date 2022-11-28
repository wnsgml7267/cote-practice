from collections import Counter

s = list(map(int, input().split()))
a = []
for i in range(1, s[0]+1):
  for j in range(1, s[1]+1):
    for k in range(1, s[2]+1):
      a.append(i+j+k)

num = Counter(a)

max_val = max(list(num.values()))

for i in list(num.keys()):
  if num[i] == max_val:
    print(i)
    break