import math
gcd, lcm = map(int,input().split()) #최대공약수, 최소공배수

def GCD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

AB = gcd * lcm #자연수 A * B == 최대공약수 * 최소공배수

for A in range(math.ceil(math.sqrt(AB)), 0, -1):
    B = AB // A
    tmpGCD = GCD(A, B)
    if tmpGCD == gcd and A // tmpGCD * B == lcm:
        print(A, AB // A)
        break

