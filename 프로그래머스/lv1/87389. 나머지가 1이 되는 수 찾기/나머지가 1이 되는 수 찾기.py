def solution(n):
    for i in range(1,n):
        a = n // i * i
        if n % a == 1:
            answer = i
            break
    return answer