import sys
input = sys.stdin.readline
n = int(input())
visited = [0 for _ in range(2000001)]
stack = []
arr = []
for i in range(1,n+1):
    a, b = map(int,input().split())
    start = a - b # 시작점 
    end = a + b # 끝점

    # 음수면 - 
    # 양수면 2배
    # -1은 1인덱스, 1은 2인덱스
    # -2는 2인덱스, 2는 4인덱스
    visited[start] = i
    visited[end] = i
for i in range(1000001, 2000001): # 음수부터 시작
    if visited[i] != 0:

        if  len(stack) == 0 or stack[-1] != visited[i]:
            stack.append(visited[i])
        elif stack[-1] == visited[i]:
            stack.pop()
for i in range(1000001):
    if visited[i] != 0:
        if  len(stack) == 0 or stack[-1] != visited[i]:
            stack.append(visited[i])
        elif stack[-1] == visited[i]:
            stack.pop()
if stack:
    print("NO")
else:
    print("YES")