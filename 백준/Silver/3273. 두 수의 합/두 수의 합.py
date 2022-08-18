import sys
input = sys.stdin.readline
n = int(input())
array = sorted(list(map(int,input().split())))
x = int(input())
cnt = 0
if len(array) == 1:
  print(cnt)
else:
  for i in range(len(array)-1):
    for j in range(i+1,len(array)):
      if array[i]+array[j] > x:
        break
      elif array[i]+array[j] == x:
        cnt += 1
        break
  print(cnt)
    
  