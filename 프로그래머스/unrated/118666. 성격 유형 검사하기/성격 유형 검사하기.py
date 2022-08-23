from random import choices
def solution(survey, choices):
    answer = ''
    per = ["RT", "CF", "JM", "AN"]
    dict = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i in range(len(survey)):
        if choices[i] < 4:
            score = 4-choices[i] #1->3 2->2 3->1
            dict[survey[i][0]] += score
        elif choices[i] > 4:
            score = choices[i]-4
            dict[survey[i][1]] += score
    for i in range(len(per)):
        if dict[per[i][0]] >= dict[per[i][1]]:
            answer += per[i][0]
        else:
            answer += per[i][1]          
    return answer