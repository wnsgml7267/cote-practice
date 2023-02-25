n, m = map(int,input().split()) # 0 ~ n-1 사람 번호, 친구 관계 수
answer = 0
graph = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(node, depth):
    global answer
    if depth == 4:
        answer = 1
        return
    
    for i in range(len(graph[node])):
        if not visited[graph[node][i]]:
            visited[graph[node][i]] = True
            dfs(graph[node][i], depth + 1)           
            visited[graph[node][i]] = False


for i in range(n-1):
    visited = [False] * n
    visited[i] = True

    dfs(i, 0) # 시작지점, 깊이(모두 친구인지)
    if answer == 1:
        break
print(answer)