N = int(input())
# 각 리스트 인덱스가 x축, 해당 인덱스 값이 y축
coordinate = [0]*N
#총 경우의 수
count = 0
# 같은 y축 혹은 대각선에 위치해있는지 판단
def judgment(x):
  for i in range(x):
    #탐색 판단할 때 x축이 같거나, 대각선일 경우 False
    if coordinate[x] == coordinate[i] or abs(coordinate[x]-coordinate[i]) == abs(x-i):
      return False
  return True
#0,0좌표부터 차례대로 모든 경우의 수 탐색
def back(x):
  global count
  #제대로 N개 만큼 도착한 경우 count + 1
  if x == N:
    count +=1  
  else:
    #모든 x좌표 차례대로 탐색
    for i in range(N):
      coordinate[x] = i
      #조건에 만족한다면 그 다음 x+1축부터 차례대로 탐색
      if judgment(x) == True:
        back(x+1)
back(0)
print(count)