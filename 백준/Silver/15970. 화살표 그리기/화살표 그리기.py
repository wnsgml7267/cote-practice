n=int(input()) #1<=N<=5000
array = [[] for i in range(5001)] #1<=색깔 종류<=N
ans=[]
answer = 0
for i in range(n):
  x,y = map(int,input().split())
  ans.append([y,x])
ans.sort()
temp = 1 #1<=색깔<=N
for i in range(len(ans)):
  if ans[i][0] != temp: #색깔이 다를 경우 해당 색깔로 변경
    temp = ans[i][0]
    array[temp].append(ans[i][1]) #해당 색깔에 점 위치 넣기
  else:
    array[temp].append(ans[i][1]) #해당 색깔에 점 위치 넣기
for i in range(1, temp+1):
  if len(array[i]) == 2:
    answer += 2*(array[i][1] - array[i][0])
    continue
  elif len(array[i])==0:
    continue
  for j in range(1,len(array[i])-1):
    answer += min(array[i][j] - array[i][j-1], array[i][j+1]-array[i][j])
  answer += array[i][1] - array[i][0]
  answer += array[i][-1] - array[i][-2]
print(answer)