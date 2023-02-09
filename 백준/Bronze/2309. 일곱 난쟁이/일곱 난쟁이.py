from itertools import combinations as cb

n = []
for _ in range(9):
  n.append(int(input()))
a=0

for i in list(cb(n,7)):

  if sum(i) == 100:
    for j in sorted(list(i)):
      print(j)
    break