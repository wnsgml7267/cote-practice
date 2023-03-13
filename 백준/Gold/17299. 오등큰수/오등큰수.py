from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))
dict = defaultdict(int)
answer = [-1] * n
stack = []
for i in arr:
    dict[i] += 1

for i in range(n):
    while stack and dict[arr[stack[-1]]] < dict[arr[i]]:
        answer[stack.pop()] = arr[i] # NGF 기록
    stack.append(i)
print(*answer)