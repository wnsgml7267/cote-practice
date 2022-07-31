from itertools import combinations as cb
switch, lamp = map(int,input().split())
switch_list = []
answer = False
for i in range(switch):
  link = list(map(int,input().split()))
  link = link[1:]
  switch_list.append(link)
array = list(cb(switch_list, switch-1))
for i in range(len(array)):
  ar = []
  for j in range(switch-1):
    ar.extend(array[i][j])
  ar = set(ar)
  if len(ar) != lamp:
    continue
  else:
    answer = True
if answer == True:
  print(1)
else:
  print(0)