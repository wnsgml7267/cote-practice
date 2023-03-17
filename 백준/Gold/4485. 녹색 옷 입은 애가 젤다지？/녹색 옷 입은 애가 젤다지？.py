from heapq import heappop, heappush
t, dx, dy = 1, (1,-1,0,0), (0,0,1,-1)
while True:
  n = int(input())
  if n == 0: break
  graph = [list(map(int,input().split())) for _ in range(n)]
  
  def dijkstra():

    min_graph = [[10**9 for _ in range(n)] for _ in range(n)]
    min_graph[0][0] = graph[0][0]
    hq = [] 
    heappush(hq, (min_graph[0][0], 0, 0))
    while hq:
      cost, x, y = heappop(hq)
      
      if x == n-1 and y == n-1:
        return min_graph[x][y]
      
      for i in range(4):
        nx, ny = dx[i] + x, dy[i] +y
        if 0 <= nx < n and 0 <= ny < n and min_graph[nx][ny] > cost + graph[nx][ny]:
          min_graph[nx][ny] = cost + graph[nx][ny]
          heappush(hq, (min_graph[nx][ny], nx, ny))
  
  print("Problem %d:" % t, dijkstra())
  t += 1