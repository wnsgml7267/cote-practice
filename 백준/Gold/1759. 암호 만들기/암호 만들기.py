from itertools import combinations
a=[]
L,C=map(int, input().split())
pwd=sorted(list(input().split()))
pos=combinations(pwd, L)
m=['a', 'e', 'i', 'o', 'u']
for i in pos:
  mo=0
  ja=0
  for j in range(len(i)):
    if i[j] in m:
      mo += 1
    else:
      ja += 1
  if mo >= 1 and ja >= 2:
    print(''.join(i))