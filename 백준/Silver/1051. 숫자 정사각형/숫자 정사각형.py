import sys
input = sys.stdin.readline
n,m = map(int,input().split())
square = []
answer = 0
for _ in range(n):
  square.append(input())

def search(x):
  for i in range(n):
    for j in range(m):
      if (i+x) < n and (j+x) < m:
        if square[i][j] == square[i][j+x] == square[i+x][j] == square[i+x][j+x]:
          print((x+1)**2)
          exit()
  search(x-1)
length = min(n,m)-1
search(length)
  
