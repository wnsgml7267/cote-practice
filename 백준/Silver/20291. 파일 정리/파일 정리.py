import sys
input=sys.stdin.readline
n=int(input())
files = dict()
for _ in range(n):
  extension = (input().split("."))[1] #확장자
  if not extension in files:
    files[extension] = 1
  else:
    files[extension] += 1
s_file = sorted(files.items()) #키 오름차순
for k,v in s_file:
  print(k.rstrip(), v)

