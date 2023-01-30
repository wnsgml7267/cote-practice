n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(3):
        if j == 0:
            graph[i][j] = min(graph[i][j] + graph[i-1][j+1], graph[i][j] + graph[i-1][j+2])
        elif j == 1:
            graph[i][j] = min(graph[i][j] + graph[i-1][j+1], graph[i][j] + graph[i-1][j-1])
        elif j == 2:
            graph[i][j] = min(graph[i][j] + graph[i-1][j-1], graph[i][j] + graph[i-1][j-2])
print(min(graph[-1]))