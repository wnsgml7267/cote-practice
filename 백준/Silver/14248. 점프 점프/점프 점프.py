n = int(input())
bridge = list(map(int,input().split()))
start = int(input())
visited = [0 for _ in range(n)]

def jump(start):
  visited[start] = 1
  left = start-bridge[start]
  right = start+bridge[start]
  if left >= 0 and visited[left] == 0:
    jump(left)
  if right < n and visited[right] == 0:
    jump(right)
jump(start-1)
print(visited.count(1))