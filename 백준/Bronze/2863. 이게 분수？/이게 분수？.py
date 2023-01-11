a, b = map(int,input().split())
c, d = map(int,input().split())

answer = []
re = a/c + b/d
cnt = 0
answer.append(c/d + a/b)
answer.append(d/b + c/a)
answer.append(b/a + d/c)
for i in range(len(answer)):
    if re < answer[i]:
        re = answer[i]
        cnt = i+1
print(cnt)        

