n, m = map(int,input().split())
if n % 2 == 0 or m % 2 == 0:
    print(n*m)
else:
    print(n*m-1)