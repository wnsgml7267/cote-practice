import sys
input = sys.stdin.readline
dot = int(input()) #점의 개수
x,y=map(int,input().split()) #가로,세로
array = set() #점 리스트
cnt = 0
for i in range(dot):
  array.add(tuple(map(int,input().split())))
for i in array:
  if (i[0]+x,i[1]) in array and (i[0]+x,i[1]+y) in array and (i[0],i[1]+y) in array:
    cnt += 1
print(cnt)