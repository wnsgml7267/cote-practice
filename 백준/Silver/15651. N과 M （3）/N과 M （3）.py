n, m = map(int,input().split())
array = []
def back(start):
    if len(array) == m:
        print(' '.join(map(str, array)))
        return
    for i in range(1, n+1):
        array.append(i)
        back(i)
        array.pop()
back(1)