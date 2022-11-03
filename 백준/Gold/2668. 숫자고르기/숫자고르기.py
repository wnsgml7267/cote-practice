import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, visit):
    visit.add(x)
    visited[x] = 1
    for i in dic[x]:
        if i not in visit:
            dfs(i, visit.copy())
        else:
            answer.extend(list(visit))
            return

n = int(input())
dic = defaultdict(list)
for i in range(1, n+1):
    dic[int(input())].append(i)

visited = [0] * (n+1)
answer = []
for i in range(1, n+1):
    if not visited[i]:
        dfs(i, set([]))

answer.sort()
print(len(answer))
for i in answer:
    print(i)