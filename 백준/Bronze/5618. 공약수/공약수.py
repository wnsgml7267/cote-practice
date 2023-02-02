import sys
input = sys.stdin.readline
import math
n=int(input())
answer = []
if n == 2:
    a, b = map(int,input().split())
    gcd =math.gcd(a,b)
    answer.append(gcd)
    for i in range(gcd-1, 0, -1):
        if a % i == 0 and b % i == 0:
            answer.append(i)
else:
    a, b, c = map(int,input().split())
    gcd = math.gcd(a,b,c)
    answer.append(gcd)
    for i in range(gcd-1, 0, -1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            answer.append(i)
for i in range(len(answer)-1,-1,-1):
    print(answer[i])

