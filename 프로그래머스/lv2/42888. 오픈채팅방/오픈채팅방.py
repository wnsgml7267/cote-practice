def solution(record):
    answer = []
    ans = []
    dic = {}
    for i in record:
        rec = i.split(" ")
        if rec[0] == "Enter":
            dic[rec[1]] = rec[2]
            ans.append([rec[1],"Enter"])
            #answer.append("%s님이 들어왔습니다." % dic[rec[1]])
        elif rec[0] == "Leave":
            ans.append([rec[1],"Leave"])
            #answer.append("%s님이 나갔습니다." % dic[rec[1]])
        else:
            dic[rec[1]] = rec[2]
    for i in ans:
        if i[1] == "Enter":
            answer.append("%s님이 들어왔습니다." % dic[i[0]])
        elif i[1] == "Leave":
            answer.append("%s님이 나갔습니다." % dic[i[0]])
    return answer