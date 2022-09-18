computer = int(input())
link = int(input())
visited = []
array = [[] for i in range(computer+1)]
for i in range(link):
  a,b = map(int, input().split())
  array[a].append(b)
  array[b].append(a)
def bfs(start):
  q = [start]
  while q:
    for i in array[q.pop()]:
      if i not in visited:
        visited.append(i)
        q.append(i)
bfs(1)
print(len(visited)-1)
