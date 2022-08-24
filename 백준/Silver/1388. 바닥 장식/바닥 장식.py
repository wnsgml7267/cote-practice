n,m = map(int,input().split()) #세로, 가로
room = []
for i in range(n):
  room.append(input())
cnt = 0


#세로ㅣ연속된 갯수
for i in range(m): #가로 
  height = ''
  for j in range(n): #세로 
    if room[j][i] == '|':
      if height != '|':
        cnt += 1
    height = room[j][i]
      
#가로 -연속된 갯수
for i in range(n): #세로
  width = ''
  for j in range(m): #가로
    if room[i][j] == '-':
      if width != '-':
        cnt += 1
    width = room[i][j]
print(cnt)