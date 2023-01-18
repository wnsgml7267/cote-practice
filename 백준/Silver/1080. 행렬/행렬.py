n, m = map(int,input().split())
A = []
B = []
for i in range(n):
    A.append(list(input()))
for i in range(n):
    B.append(list(input()))
cnt = 0
def search(q,w):
    for i in range(q, q+3):
        for j in range(w, w+3):
            A[i][j] = str(1 - int(A[i][j]))

for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            search(i,j)
            cnt += 1
        if A == B:
            break
    if A == B:
        break
if A == B:
    print(cnt)
else:
    print(-1)
        