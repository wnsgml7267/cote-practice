import sys
sys.setrecursionlimit(10**9)

n, m = map(int,input().split())
graph = []
bool = False # 침투 여부
# 0, 1 => 흰색, 검은색

for i in range(n):
    graph.append(list(input()))

'''
1. x 좌표가 0인 경우 dfs 탐색 (outerside 이므로)
2. x 좌표가 n-1인 구역을 방문했으면 (inside 침투 완료) YES
'''
dx, dy = (1,-1,0,0), (0,0,1,-1)

def dfs(x, y):
    global bool
    if x == n-1:
        bool = True
        return
    
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == '0': # 전류 통하는 흰색
                graph[nx][ny] = -1
                dfs(nx,ny)

# 1.
for i in range(m):
    if graph[0][i] == '0':
        dfs(0,i)

# 2.
# for i in range(m):
#     if graph[-1][i] == -1: # 전류가 흘렀다면 침투 완료
#         bool = True
#         break
if bool:
    print("YES")
else:
    print("NO")