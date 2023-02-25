'''
(A,B,C,D,E,F)AFC
AFC
AFC(A,B,C,D,E,F)
(A,B,C,D,E,F)AFC(A,B,C,D,E,F)
최소 3글자, 최대 5글자
'''
str = ['A','B','C','D','E','F']
basic = 'AFC'
n = int(input())
for _ in range(n):
    s = input()
    answer = ''
    start = 'z'
    for i in s:
        if i != start:
            start = i
            answer += i
    if len(answer) == 3:
        if answer == 'AFC':
            print('Infected!')
        else:
            print('Good')
    elif len(answer) == 4:
        if answer[:3] == 'AFC' and answer[-1] in str:
            print('Infected!')
        elif answer[-3:] == 'AFC' and answer[0] in str:
            print('Infected!')
        else:
            print('Good')
    elif len(answer) == 5:
        if answer[1:4] == 'AFC' and answer[0] in str and answer[-1] in str:
            print('Infected!')
        else:
            print('Good')
    else:
        print('Good')