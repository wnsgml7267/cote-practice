import sys
input = sys.stdin.readline
dic = dict()
n = int(input())
for i in range(n):
  s = input().rstrip()
  if s not in dic:
    dic[s] = 1
  else:
    dic[s] += 1
for i in range(n-1):
  s = input().rstrip()
  dic[s] -= 1
for i in dic:
  if dic[i] == 1:
    print(i)
    break