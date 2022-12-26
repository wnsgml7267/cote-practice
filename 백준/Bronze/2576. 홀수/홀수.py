a = []
for i in range(7):
    t = int(input())
    if t % 2 == 1:
        a.append(t)
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))