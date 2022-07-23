n=int(input())
array = []
for i in range(n):
  array.append(i+1)
answer=[]
while len(array) != 1:
  answer.append(array.pop(0))
  array.append(array.pop(0))
answer.append(array[0])
print(*answer)
  