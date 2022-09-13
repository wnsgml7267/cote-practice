n,c=map(int,input().split())
array = list(map(int,input().split()))
answer = []
dic = dict()
dic[array[0]] = array.count(array[0])
temp = array[0]
for i in range(1,n):
  if array[i] != temp:
    dic[array[i]] = array.count(array[i])
    temp = array[i]
new_dic = sorted(dic.items(), key = lambda x: -x[1])
for i in new_dic:
  for j in range(i[1]):
    answer.append(i[0])
print(*answer)
