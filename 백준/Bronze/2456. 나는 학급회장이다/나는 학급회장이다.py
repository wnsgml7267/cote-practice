score = [[0]*3 for i in range(3)] #최종 점수,3점, 2점
n = int(input())
for i in range(n):
    array = list(map(int,input().split()))
    for j in range(len(array)):
        score[j][0] += array[j]
        if array[j] == 3:
            score[j][1] += 1
        elif array[j] == 2:
            score[j][2] += 1
dic = dict()
for i in range(len(score)):
    dic[i+1] = score[i]
d = sorted(dic.items(), key=lambda x:x[1], reverse=True)
if d[0][1][0] == d[1][1][0]:
    if d[0][1][1] == d[1][1][1] and d[0][1][2] == d[1][1][2]:
        print(0, d[0][1][0])
    else:
        print(d[0][0], d[0][1][0])
else:
    print(d[0][0], d[0][1][0])
