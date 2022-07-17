import sys
input = sys.stdin.readline
K, N = map(int,input().split())
line = []
for i in range(K):
  li = int(input())
  line.append(li)
start = 1
end = max(line)

while start <= end:
  cnt = 0
  mid = (end+start)//2
  for i in line:
    cnt += i//mid
  if cnt < N:
    end = mid - 1
  else:
    start = mid + 1
    
print(end)



