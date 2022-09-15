def solution(s):
    s = s[2:-2].split("},{")
    array = []
    for i in range(len(s)):
        s_array = s[i].split(",")
        array.append(set(s_array))
    
    array.sort(key=lambda x: len(x))
    
    ans = set()
    answer = []
    for i in array:
        tmp = i - ans
        answer.append(list(tmp)[0])
        ans = ans | tmp
    answer = [int(i) for i in answer]
    return answer