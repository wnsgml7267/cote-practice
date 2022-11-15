import sys
t = int(sys.stdin.readline())
for i in range(t):
    c = []
    for j in range(4):
        x, y = list(map(int,sys.stdin.readline().split()))
        c.append((x, y))
    c.sort()

    side_one = (c[0][0] - c[1][0])**2 + (c[0][1] - c[1][1])**2
    side_two = (c[1][0] - c[3][0])**2 + (c[1][1] - c[3][1])**2
    side_three = (c[3][0] - c[2][0])**2 + (c[3][1] - c[2][1])**2
    side_four = (c[2][0] - c[0][0])**2 + (c[2][1] - c[0][1])**2
    edge_one = (c[0][0] - c[3][0])**2 + (c[0][1] - c[3][1])**2
    edge_two = (c[2][0] - c[1][0])**2 + (c[2][1] - c[1][1])**2
    
    if side_one != side_two or side_two != side_three or side_three != side_four or edge_one != edge_two or side_one + side_two != edge_one:
        print(0)    
    else:
        print(1)