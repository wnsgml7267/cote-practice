t = int(input())
for i in range(t):
  n, m = map(int,input().split())
  books = []
  for i in range(m):
      a, b = map(int,input().split())
      books.append([a,b])
  books.sort(reverse=True)
  visited = [0] * 1001
  for i in books:
      aa = i[0]
      bb = i[1]
      for j in range(bb,aa-1,-1):
          if not visited[j]:
              visited[j] = 1
              break
  print(visited.count(1))