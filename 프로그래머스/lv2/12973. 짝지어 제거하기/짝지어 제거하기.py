def solution(s):
    stack = [s[0]]
    for i in range(1,len(s)):
        stack.append(s[i])
        try:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        except:
            pass
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer
