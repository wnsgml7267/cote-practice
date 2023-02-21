import sys
input = sys.stdin.readline
N = int(input())
quad = [list(map(int, input().strip())) for _ in range(N)]
#0~7
def conq(x,y,n):
  num = quad[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if quad[i][j] != num:
        print('(', end='')
        conq(x,y,n//2)
        conq(x,y+n//2, n//2)
        conq(x+n//2, y, n//2)
        conq(x+n//2, y+n//2, n//2)
        print(')', end='')
        return
  if num == 0:
    print('0',end='')
    return
  else:
    print('1', end='')
    return
conq(0,0,N)