from itertools import combinations as cb
#가진 문제 수,고른 문제 난이도합이 크거나 같, 작거나 같, 난이도 차 >= X
N,L,R,X = map(int,input().split()) 
cnt = 0
diff = list(map(int,input().split()))
#사용할 문제는 두 문제 이상.
for i in range(2,N+1):
  for j in cb(diff,i):
    if L <= sum(j) <= R and (max(j) - min(j)) >= X:
      cnt += 1
print(cnt)
    
