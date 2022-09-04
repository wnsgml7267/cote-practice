s = input()
cnt = 0
for i in range(int(input())):
    a = input() * 2
    if s in a:
        cnt += 1
print(cnt)