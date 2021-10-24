import math
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 34
b = 22

print(math.gcd(21, 14))
print(lcm(21, 14))