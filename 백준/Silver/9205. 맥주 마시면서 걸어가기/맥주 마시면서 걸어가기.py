from collections import deque
t = int(input())
for i in range(t):
    store_count = int(input())
    start_x, start_y = map(int,input().split())
    store = []
    for j in range(store_count):
        sx, sy = map(int,input().split())
        store.append((sx,sy))
    festival_x, festival_y = map(int,input().split())
    store_visited = [0 for _ in range(store_count)]
    q = deque()
    q.append((start_x,start_y))
    answer = "sad"
    while q:
        x, y = q.popleft()
        if abs(x-festival_x) + abs(y-festival_y) <= 1000:
            answer = "happy"
            break
        for k in range(store_count):
            if store_visited[k] == 0:
                sx, sy = store[k]
                if abs(x-sx) + abs(y-sy) <= 1000:
                    store_visited[k] = 1
                    q.append((sx,sy))
    print(answer)
    