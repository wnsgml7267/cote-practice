p, k = map(int, input().split())
bool = True
for i in range(2, k):
    if p % i == 0:
        print("BAD", i)
        bool = False
        break
if bool:
    print("GOOD")