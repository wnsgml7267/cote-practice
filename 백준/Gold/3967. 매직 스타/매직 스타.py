import sys
input = sys.stdin.readline
num = [1,2,3,4,5,6,7,8,9,10,11,12]
graph = [list(input().rstrip()) for _ in range(5)]
arr = []
cnt = 0
visited = [False] * 13
xy = []
# result = copy.deepcopy(graph)
for i in range(5):
    for j in range(9):
        if graph[i][j] == '.': continue
        elif graph[i][j] == 'x':
            arr.append(0)
            xy.append((i,j))
        else: 
            xy.append((i,j))
            arr.append(ord(graph[i][j])-64)
            visited[(ord(graph[i][j])-64)] = True
            cnt += 1

def check():
    one = arr[0] + arr[2] + arr[5] + arr[7]
    two = arr[7] + arr[8] + arr[9] + arr[10]
    thr = arr[10] + arr[6] + arr[3] + arr[0]
    four = arr[1] + arr[2] + arr[3] + arr[4]
    five = arr[1] + arr[5] + arr[8] + arr[11]
    six = arr[4] + arr[6] + arr[9] + arr[11]
    if one == 26 and two == 26 and thr == 26 and four == 26 and five == 26 and six == 26:
        return True
    return False

def dfs(idx, n):
    global cnt
    # print(n, cnt)
    if n == (12-cnt):
        
        if check():
            id = 0
            while id < 12:
                for j in range(5):
                    for k in range(9):
                        if graph[j][k] != '.':
                            graph[j][k] = chr(arr[id]+64)
                            id += 1
            for l in range(5):
                print(''.join(graph[l]))
                
            exit(0)
            return
        return
        
    if arr[idx] == 0:
        for i in range(1,13):
            if not visited[i]:
                visited[i] = True
                arr[idx] = i
                dfs(idx + 1, n + 1)
                arr[idx] = 0
                visited[i] = False
                
                # st.remove(i)
    else:
        dfs(idx+1, n)
    

dfs(0,0)