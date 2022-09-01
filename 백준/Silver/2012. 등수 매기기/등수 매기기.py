n = int(input())
array = []
for i in range(n):
  ex = int(input())
  array.append(ex)
array.sort()

cnt = 0
for i in range(1,n+1):
  cnt += abs(i-array[i-1])
print(cnt)