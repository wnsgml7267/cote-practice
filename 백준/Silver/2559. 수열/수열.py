n,k=map(int, input().split())
array = list(map(int,input().split()))
first_sum = sum(array[:k])
ans = [first_sum]
for i in range(1,n-(k-1)):
  first_sum = first_sum - array[i-1] + array[i+(k-1)]
  ans.append(first_sum)
print(max(ans))