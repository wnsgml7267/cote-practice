for _ in range(int(input())):
    a, b = input().split('-')
    n = int(b)
    s = 0
    for i in range(3):
        s += (ord(a[i]) - 65) * 26 ** (2-i)
    print("nice" if abs(s-n) <= 100 else "not nice")