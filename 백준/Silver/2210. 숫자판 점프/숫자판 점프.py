import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

graph = []
for i in range(5):
    graph.append(list(map(str,input().split())))

dx = (1,-1,0,0)
dy = (0,0,1,-1)

def dfs(x,y,str_num):

    str_num += graph[x][y]

    if len(str_num) == 6:
        if str_num not in answer:
            answer.append(str_num)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx,ny,str_num)
            
answer = []
for i in range(5):
    for j in range(5):
        dfs(i,j,'')
            
print(len(answer))