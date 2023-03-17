import sys
input = sys.stdin.readline
from heapq import heappop, heappush
t = int(input())
for i in range(t):
    n, d, c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    min_graph = [10**9] * (n+1)
    hq = []
    for j in range(d):
        a, b, time = map(int,input().split())
        graph[b].append([a,time])

    def dijk(c):
        heappush(hq, (0, c))
        min_graph[c] = 0
        while hq:
            vr, num = heappop(hq)
            for k in graph[num]:
                # k[0] : 의존 번호, k[1] : 바이러스 시간
                if k[1] + vr < min_graph[k[0]]:
                    min_graph[k[0]] = k[1] + vr
                    heappush(hq, (min_graph[k[0]], k[0]))

    dijk(c)

    computer_cnt = 0
    virus = 0                
    for l in min_graph:
        if l != 10**9: # 감염 되었을 때
            computer_cnt += 1
            virus = max(virus, l)
    print(computer_cnt, virus)