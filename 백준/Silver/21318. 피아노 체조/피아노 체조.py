import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int,input().split()))
add = [0]*n
for i in range(1,n):
  if array[i-1] > array[i]:
    add[i] = add[i-1] + 1
  else:
    add[i] = add[i-1]
test = int(input())
for _ in range(test):
  x, y =map(int,input().split())
  print(add[y-1] - add[x-1])