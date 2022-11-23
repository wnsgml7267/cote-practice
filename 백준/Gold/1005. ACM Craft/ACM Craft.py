from collections import deque
T = int(input())
for _ in range(T):
    N, K = map(int,input().split()) #건물 개수, 건설 규칙 개수 => 건물 번호는 1~N번
    build_time = [0] + list(map(int,input().split())) #건물 당 건설에 걸리는 시간
    build = [[] for _ in range(N+1)] #건물 번호 1~N번
    inde = [0 for _ in range(N+1)] #진입차수
    dp = [0 for _ in range(N+1)]
    
    for i in range(K):
        x, y = map(int,input().split())
        build[x].append(y)
        inde[y] += 1
    
    endpoint = int(input()) #도착 지점

    q = deque()
    for i in range(1, N+1): #진입차수 0인 것 큐에 넣기(출발 지점)
        if inde[i] == 0:
            q.append(i)
            dp[i] = build_time[i]
    
    while q:
        tmp = q.popleft()
        
        for j in build[tmp]:
            inde[j] -= 1 #진입차수 줄이기
            dp[j] = max(dp[tmp] + build_time[j], dp[j])
            if inde[j] == 0:
                q.append(j)
    print(dp[endpoint])
            


