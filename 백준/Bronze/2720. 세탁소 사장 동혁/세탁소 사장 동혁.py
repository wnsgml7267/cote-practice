n = int(input())
for i in range(n):
    a = int(input())
    q = a // 25
    a = a % 25
    d = a // 10
    a %= 10
    n = a // 5
    a %= 5
    print(q,d,n,a)
