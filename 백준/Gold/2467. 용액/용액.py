n = int(input())
array = list(map(int,input().split()))
special_value = float('inf')
start, end = 0, n-1
while start < end:
    sum_value = array[start] + array[end]
    if abs(sum_value) < special_value:
        left = start
        right = end
        special_value = abs(sum_value)
    if sum_value < 0:
        start += 1
    elif sum_value > 0:
        end -= 1
    else:
        break
print(array[left], array[right])