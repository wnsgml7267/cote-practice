n, m = map(int,input().split())
arr = list(map(int,input().split()))

answer= []

sm = 0
for i in range(len(arr)):
  arr[i] = sm + arr[i]
  sm = arr[i]

answer.append(arr[m-1])

for i in range(1, n-m+1):
  answer.append(arr[i+m-1] - arr[i-1])

mx = max(answer)
if not mx:
  print("SAD")
else:
  print(mx)
  print(answer.count(mx))