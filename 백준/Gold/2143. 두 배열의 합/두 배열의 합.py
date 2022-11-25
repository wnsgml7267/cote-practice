from collections import Counter

T = int(input())
N = int(input())
N_arr = list(map(int,input().split()))
M = int(input())
M_arr = list(map(int,input().split()))

cnt = 0
c = Counter()

for i in range(N):
    for j in range(i, N):
        c[sum(N_arr[i:j+1])] += 1 #같은 Key가 있을 수 있으므로 += 1
for i in range(M):
    for j in range(i, M):
        cnt += c[T-sum(M_arr[i:j+1])]
print(cnt)