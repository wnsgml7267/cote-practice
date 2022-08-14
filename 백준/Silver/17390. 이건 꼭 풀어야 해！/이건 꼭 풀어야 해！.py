import sys
input = sys.stdin.readline
n,q = map(int,input().split()) #수열 길이, 질문의 개수
a = sorted(list(map(int,input().split()))) #수열

for i in range(1, len(a)):
  a[i] = a[i] + a[i-1] #연속된 합 구해놓기
for i in range(q):
  l, r = map(int,input().split()) #욱제의 질문
  if l == 1:
    print(a[r-1])
  else:
    print(a[r-1]-a[l-2])