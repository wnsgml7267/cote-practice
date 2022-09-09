n = int(input())
candy = []
for i in range(n):
  candy.append(list(input()))
answer = 1
def search(candy):
  global answer
  for i in range(n):
    cnt = 1
    for j in range(1,n):
      if candy[i][j] == candy[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      answer = max(answer,cnt)
    cnt = 1
    for j in range(1,n):
      if candy[j][i] == candy[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      answer = max(answer,cnt)
for i in range(1,n):
  for j in range(1,n):
    candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]
    search(candy)
    candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]
    
    candy[j][i], candy[j-1][i] = candy[j-1][i], candy[j][i]
    search(candy)
    candy[j][i], candy[j-1][i] = candy[j-1][i], candy[j][i]
print(answer)