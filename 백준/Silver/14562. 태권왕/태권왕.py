from collections import deque
t = int(input())


for i in range(t):
    a, b = map(int,input().split())
    visited = [0] * (200)
    q = deque()
    q.append((a,b,0))
    while q:
        x, y, z = q.popleft() #A, B, 최소 연속 발차기 횟수
        
        if x <= y:
            q.append((x*2, y+3, z+1))
            q.append((x+1, y, z+1))
            if x == y:
                print(z)
                break