from collections import deque
n = int(input())
array = []
a = deque()
for i in range(n):
    s = deque(input())
    a.append(s)
    
while a:
    cnt = 0
    tmp = a.popleft()
    for i in range(len(tmp)):
        tmp.append(tmp.popleft())
        if tmp in array:
            cnt += 1
    if cnt == 0:
        array.append(tmp)
print(len(array))
            