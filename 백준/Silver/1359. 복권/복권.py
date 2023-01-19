from itertools import combinations as cb
N, M, K = map(int,input().split())

N_arr = []
answer = 0

for i in range(1,N+1):
    N_arr.append(i)

#1~N 중에 서로 다른 M개 : 조합 NCM == 전체 경우의 수
for i in list(cb(N_arr,M)):
    count = 0
    for j in range(M):
        if i[j] <= M: # 당첨번호가 1~M 이라고 가정.
            count += 1
    if count >= K: #당첨번호가 적어도 K개 이상 같을 때
        answer += 1
print(answer / len(list(cb(N_arr,M)))) # 당첨번호가 K개 이상 같을 때 // 전체 경우의 수