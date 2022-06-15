import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start = 1
end = max(tree)
while start <= end:
  length = 0
  height = (start+end)//2
  for i in tree:
    if i > height:
      length += i-height
  if length >= M:
    start = height + 1
  else:
    end = height - 1
print(end)