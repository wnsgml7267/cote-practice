N = int(input())
m = input()
count = m.count('LL')
if (count <= 1):
    print(len(m))
else:
    print(len(m) - count + 1)