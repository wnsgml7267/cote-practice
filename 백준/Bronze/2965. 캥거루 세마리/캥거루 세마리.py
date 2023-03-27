arr = list(map(int,input().split()))
a = arr[0]
b = arr[1]
c = arr[2]
print(max((b-a), (c-b)) - 1)