import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 삭제된 노드면 계속 제거
def pp(arr):
    while arr and not visited[arr[0][1]]:
        heappop(arr)

t = int(input())
for i in range(t):
    n = int(input())
    q = [] # 우선순위 큐 저장 
    q1 = [] # 역 우선순위 큐 저장
    visited = [False] * (10**6+1) # False : 큐에 해당 인덱스 원소가 없음
    for idx in range(n):
        str, num = input().split()
        num = int(num)
        if str == 'I':
            heappush(q, (num, idx))
            heappush(q1, (-num, idx))
            visited[idx] = True # 큐에 해당 원소 존재
      
        else:
            if num == -1: # 최솟값 삭제
                pp(q)
                if q:
                    visited[q[0][1]] = False
                    heappop(q)
                
            else: # 최댓값 삭제
                pp(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heappop(q1)
    pp(q)
    pp(q1)
  # 큐가 비어있지 않다면 최댓값과 최솟값 출력
    if q and q1:
        print(-heappop(q1)[0], heappop(q)[0])
    else: # 비어있다면 EMPTY
        print("EMPTY")