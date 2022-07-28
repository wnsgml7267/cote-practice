from itertools import combinations_with_replacement as cb
n = int(input())
result = []
array = [1, 5, 10, 50]
for temp in cb(array, n):
    result.append(sum(temp))
print(len(set(result)))