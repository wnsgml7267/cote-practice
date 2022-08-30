import sys
input = sys.stdin.readline
n,m=map(int,input().split()) #점, 선분
dot = sorted(list(map(int,input().split()))) #점
for i in range(m): #선분 좌표
  x, y = map(int, input().split()) #시작점, 끝점
  start = 0
  end = n-1
  start1=0
  end1=n-1
  while start <= end:
    mid = (start+end)//2
    if dot[mid] < x:
      start = mid+1
    else:
      end = mid-1
  end += 1 #시작 인덱스
  while start1 <= end1:
    mid1 = (start1+end1)//2
    if dot[mid1] <= y:
      start1 = mid1+1
    else:
      end1 = mid1-1
  print(end1-end+1)
  
