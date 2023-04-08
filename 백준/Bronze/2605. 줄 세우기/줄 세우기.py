n = int(input())
arr = list(map(int,input().split()))
answer = []
for i in range(n):
    answer.insert(i-arr[i], i+1)
    
for j in answer:
    print(j, end = ' ')