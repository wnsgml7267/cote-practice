'''
탑의 수 : 1 ~ 500,000
탑들의 높이 : 1 ~ 100,000,000

0 1 2 3 4
6 9 5 7 4
0 0 2 2 4

현재 값보다 이전값이 작으면 스택에서 pop, 크면 해당 인덱스 저장 후, 현재 값 스택에서 append
'''

n = int(input())
arr = list(map(int,input().split()))
idx = 1
stack = [arr[0]]
answer = [0]

dic = {}
for i in range(n):
    dic[arr[i]] = i+1

for i in range(1,n):
    if stack[-1] < arr[i]:
        while(stack[-1] < arr[i]): # 현재값이 더 크면 큰거 찾을때까지 반복
            stack.pop()
            if len(stack) == 0:
                break
        if len(stack) == 0: 
            stack.append(arr[i])
            answer.append(0)
        else:
            answer.append(dic[stack[-1]])
            stack.append(arr[i])
    elif stack[-1] > arr[i]: # 현재값이 더 작으면
        answer.append(dic[stack[-1]])
        stack.append(arr[i])
print(' '.join(map(str, answer)))



