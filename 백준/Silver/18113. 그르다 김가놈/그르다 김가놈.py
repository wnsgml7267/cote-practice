n, k, m = map(int, input().split())
array = []
answer = -1
for i in range(n):
    kimbap = int(input())
    if kimbap > 2 * k:  #두 꼬다리
        array.append(kimbap - 2 * k)
    elif k < kimbap < 2 * k:  #한 꼬다리
        array.append(kimbap - k)
if len(array) == 0:
    print(-1)
    exit(0)
  
start, end = 1, max(array)

while start <= end:
    mid = (start + end) // 2
    total = sum([i//mid for i in array])
    if total >= m:  #m개 보다 더 만들어지면
        answer = mid
        start = mid + 1
    elif total < m:  #m개 보다 적으면
        end = mid - 1
print(answer)
