import sys
input = sys.stdin.readline
cow, costume = map(int,input().split()) #소 마리 수, 코스튬
cow_array = []
cnt = 0
for i in range(cow):
  cow_array.append(int(input()))
cow_array.sort()
for i in range(cow-1):
  for j in range(i+1,cow):
    if cow_array[i] + cow_array[j] <= costume:
      cnt += 1
    else:
      break
print(cnt)