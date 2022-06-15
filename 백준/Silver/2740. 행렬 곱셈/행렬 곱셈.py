A=[]
B=[]
n,m=map(int,input().split())
for i in range(n):
  A.append(list(map(int,input().split())))
m,k=map(int,input().split())
for j in range(m):
  B.append(list(map(int,input().split())))
#행렬 곱셈 -> n*m행렬 x m*k행렬 = n*k행렬
C=[[0 for _ in range(k)] for _ in range(n)]
for N in range(n):
  for K in range(k):
    for M in range(m):
      C[N][K] += A[N][M] * B[M][K]
for i in C:
  for j in i:
    print(j, end = ' ')
  print()