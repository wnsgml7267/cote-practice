W, H, X, Y, P = map(int,input().split())
R = H/2 #반지름
cnt = 0
for i in range(P):
  man_x, man_y = map(int,input().split())
  left = ((man_x - X) ** 2 + (man_y - (Y + R)) ** 2) ** 0.5 #왼쪽 반원
  right = ((man_x - (X + W)) ** 2 + (man_y - (Y + R)) ** 2) ** 0.5 #오른쪽 반원
  if ((X <= man_x <= X+W) and (Y <= man_y <= Y+H)) or (left <= R or right <= R):
    cnt += 1
print(cnt)
    