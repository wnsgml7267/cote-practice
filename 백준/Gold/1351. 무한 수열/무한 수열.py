n, p, q = map(int,input().split())
dict = {0:1}

def A(n):    
    if n in dict:
        return dict[n]
    
    dict[n] = A(n//p) + A(n//q)
    return dict[n]
print(A(n))