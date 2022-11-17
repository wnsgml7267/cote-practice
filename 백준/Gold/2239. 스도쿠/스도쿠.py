from sys import stdin
input = stdin.readline

# 행 체크
def rowCheck(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True

# 열 체크
def colCheck(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

# 3 * 3 체크
def squareCheck(r, c, num):
    nr = (r//3) * 3
    nc = (c//3) * 3
    for i in range(3):
        for j in range(3):
            if board[nr+i][nc+j] == num:
                return False
    return True

def dfs(depth):
    if depth == len(zeros): #0을 모두 숫자로 다 채웠을 경우 출력
        for row in range(9):
            for col in range(9):
                print(board[row][col], end="")
            print()
        exit()
    
    nr, nc = zeros[depth]	# 현재 확인할 위치
    for num in range(1, 10):
        if rowCheck(nr, num) and colCheck(nc, num) and squareCheck(nr, nc, num):
            board[nr][nc] = num
            dfs(depth + 1)
            board[nr][nc] = 0


board = []# 스도쿠 보드
zeros = []# 0 위치 담기
#9x9
for r in range(9):
    board.append(list(map(int, input().rstrip())))
    for c in range(9):
        if board[r][c] == 0:
            zeros.append((r, c)) #0의 위치 기록
dfs(0)