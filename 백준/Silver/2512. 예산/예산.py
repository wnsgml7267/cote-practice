n = int(input())
array = list(map(int,input().split()))
total_budget = int(input())
start = 0
end = max(array)

while start <= end:
  mid = (start+end)//2
  use_budget = 0
  for i in array:
    if i < mid:
      use_budget += i
    else:
      use_budget += mid
  if total_budget >= use_budget:
    start = mid + 1
  else:
    end = mid - 1
print(end)