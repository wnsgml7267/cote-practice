n, p, q = map(int,input().split())
A = {0:1}
def result(n):
    if n in A:
        return A[n]
    A[n] = result(n//p) + result(n//q)
    return A[n]
print(result(n))