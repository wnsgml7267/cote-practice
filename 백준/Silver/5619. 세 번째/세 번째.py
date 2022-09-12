from itertools import permutations
n = int(input())
answer = set()
for i in range(n):
  answer.add(int(input()))
answer = list(answer)
answer.sort()
ans = []
a = list(permutations(answer[:4], 2))
for i in a:
  ans.append(int(str(i[0])+str(i[1])))
ans.sort()
print(ans[2])