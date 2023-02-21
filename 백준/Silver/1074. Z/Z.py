N, r, c = map(int, input().split())
cnt = 0

def conquer(x, y ,size):
    global r, c, cnt
    if size == 1:
        return
    
    newSize = size // 2

    # 1 사분면
    if r < (x + newSize) and c < (y + newSize):
        conquer(x, y, newSize)
    # 2 사분면
    if r < (x + newSize) and c >= (y + newSize):
        cnt += size * size // 4
        conquer(x, y + newSize, newSize)
    if r >= (x + newSize) and c < (y + newSize):
        cnt += size * size // 4 * 2
        conquer(x+newSize, y, newSize)
    if r >= (x + newSize) and c >= (y + newSize):
        cnt += size * size // 4 * 3
        conquer(x+newSize, y+newSize, newSize)        

conquer(0,0,2**N)
print(cnt)