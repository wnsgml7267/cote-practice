x = int(input())
for i in range(x):
    num = []
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            num.append(i)
    print(sum(num), min(num))