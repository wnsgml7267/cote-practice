def colOk(num, x):
    for i in range(9):
        if sudoku[x][i] == num:
            return False
    return True

def rowOk(num, y):
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True

def squareOk(num, x, y):
    nx = (x//3) * 3
    ny = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[nx+i][ny+j] == num:
                return False
    return True
def dfs(d):
    if d == len(zero):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end='')
            print()
        exit()
    x, y = zero[d]
    for num in range(1,10):
        #행, 열, 3x3 중복 체크
        if colOk(num,x) and rowOk(num,y) and squareOk(num,x,y):
            sudoku[x][y] = num
            dfs(d+1)
            sudoku[x][y] = 0
sudoku = []
zero = []
for i in range(9):
    sudoku.append(list(map(int, input().rstrip())))
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append((i,j))
dfs(0)
