m = int(input())
array = list(map(int, input().split()))
array.sort()
answer = []
for i in range(len(array)//2):
  if m % 2 == 0:
    answer.append(array[i]+array[-(i+1)])
  else:
    answer.append(array[i]+array[-(i+2)])
print(max(answer))
