from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append((a, ""))

  while q:
    num, result = q.popleft()
    
    #D
    d = (num * 2) % 10000
    if d == b:
      return result + "D"
    elif graph[d] == 0:
      graph[d] = 1
      q.append((d, result + "D"))

    #S
    if num == 0:
      s = 9999
    else:
      s = num - 1
    if s == b:
      return result + "S"
    elif graph[s] == 0:
      graph[s] = 1
      q.append((s, result + "S"))

    #L
    l = int(num % 1000 * 10 + num / 1000)
    if l == b:
      return result + "L"
    elif graph[l] == 0:
      graph[l] = 1
      q.append((l, result + "L"))

    r = int(num % 10 * 1000 + num // 10)
    if r == b:
      return result + "R"
    elif graph[r] == 0:
      graph[r] = 1
      q.append((r, result + "R"))

n = int(input())
for i in range(n):
  a, b = map(int,input().split())
  graph = [0] * 10000
  print(bfs())