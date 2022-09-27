n = int(input())
array = []
dic = dict()
for i in range(n):
  s =input()
  array.append(s)

for i in range(n):
  cnt = 0
  for j in range(len(array[i])):
    if array[i][j].isdigit():
      cnt += int(array[i][j])
  dic[array[i]] = cnt
#길이 오름차순
array = sorted(array, key = lambda x:(len(x), dic[x], x))
for i in array:
  print(i)
  