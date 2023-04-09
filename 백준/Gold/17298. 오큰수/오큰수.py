n = int(input())
arr = list(map(int,input().split()))
answer = [-1 for _ in range(n)]
stack = []
for i in range(n-2, -1, -1):
    if arr[i] < arr[i+1] and arr[i] < answer[i+1]: # 바로 뒤에 있는 값이 크면
      answer[i] = arr[i+1]
      stack.append(answer[i+1])
    elif arr[i] < arr[i+1]:
       answer[i] = arr[i+1]
    elif arr[i] < answer[i+1]: # 이전에 있던 값중 큰 수
      answer[i] = answer[i+1]
    else: # 둘 다 작을 때
      while(stack):
         p = stack.pop()
         if arr[i] < p:
            answer[i] = p
            break
       
print(*answer)