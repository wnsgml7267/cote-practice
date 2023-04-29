from collections import defaultdict as dd    
n = int(input())
numbers = list(map(int,input().split()))
answer = ''
dic = dd(list)
num_arr = []
for num in numbers:
    dic[str(num)[0]].append([int((str(num)*10)[:10]), str(num)])
            
for i in dic.keys():
    num_arr.append(i)
    dic[i].sort(reverse=True)

num_arr.sort(reverse=True)
for i in num_arr:
    for j in dic[i]:
        answer += j[1]
print(str(int(answer)))