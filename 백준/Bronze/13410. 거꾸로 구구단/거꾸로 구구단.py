answer = 0
n, m = map(int,input().split())
for i in range(1,m+1):
  answer = max(answer, int(str(n*i)[::-1]))
print(answer)
          