import sys
input = sys.stdin.readline
n,m,r = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

def rot(x,y):
  global temp
  prev_value = graph[x][y] #현재 값 저장
  graph[x][y] = temp #회전
  temp = prev_value #이전 값 저장
  
  
for _ in range(r): #회전 수
  for i in range(min(n, m) // 2): #돌려지는 갯수
    x,y=i,i
    temp = graph[x][y] #시작 값 저장

    for k in range(i+1, n-i): #왼쪽
      x = k #행을 바꿔주기 위함
      rot(x,y)

    for k in range(i+1, m-i): #아래
      y = k
      rot(x,y)

    for k in range(i+1, n-i): #오른쪽
      x = n - k - 1  #행이 감소
      rot(x,y)

    for k in range(i+1, m-i): #
      y = m - k - 1  #열이 감소
      rot(x,y)

for i in range(n):
  print(*graph[i])
