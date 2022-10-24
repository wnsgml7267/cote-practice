answer = []
for i in range(5):
    a = int(input())
    answer.append(a)
answer.sort()
print(sum(answer)//5, answer[2])
    