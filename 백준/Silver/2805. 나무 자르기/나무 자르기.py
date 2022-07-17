import sys
input = sys.stdin.readline
n,h=map(int,input().split())
tree = list(map(int,input().split()))
start, end = 0, max(tree)
while start <= end:
  mid = (start+end)//2
  tree_get = 0
  for i in tree:
    if i > mid:
      tree_get += i-mid
  if tree_get < h:
    end = mid - 1
  else:
    start = mid + 1
print(end)