aa = int(input())
while True:
    flag = True
    for i in str(aa):
        if i!="4" and i!="7":
            flag = False
            aa -= 1
    if flag :
        print(aa)
        break