from collections import deque
n, k = map(int,input().split())
a = deque(str(i) for i in range(1,n+1))
result = []
while a:
    for i in range(k-1):
        a.append(a.popleft())
    result.append(a.popleft())
print('<'+', '.join(result)+'>')