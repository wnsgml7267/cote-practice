while True:
    n = input()
    if n == '0':
        break
    while len(n) > 1:
        num = 0
        for i in n:
            num += int(i)
        n = str(num)
    print(n)