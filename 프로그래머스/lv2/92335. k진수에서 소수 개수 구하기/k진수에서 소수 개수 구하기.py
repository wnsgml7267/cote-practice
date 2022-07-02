def div(n, k):  # n을 k진수로 반환
    ret = ""
    while n > 0:
        ret += str(n % k)
        n = n //  k
    return ''.join(reversed(ret))
def is_prime_num(k):
    if k == 2 or k == 3: return True  # 2 or 3 은 소수
    if k % 2 == 0 or k < 2: return False  # 2의 배수이거나 2보다 작은 값인 
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

def solution(n, k):
    count = 0
    a = div(n,k).split("0")
    for i in a:
        if i == "" : continue
        if is_prime_num(int(i)) == True:
            count += 1
    return count