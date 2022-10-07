while True:
    a = sorted(list(map(int, input().split())))
    if sum(a) == 0:
        break
    if a[-1]**2 == a[0]**2 + a[1]**2:
        print("right")
    else:
        print("wrong")