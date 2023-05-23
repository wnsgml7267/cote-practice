for k in range(int(input())):
    s = input()
    tmp = ''
    for i in range(len(s)):
        if i % 2 == 0 :
            tmpnum=2*int(s[i])
            if tmpnum>9: tmpnum= tmpnum%10+tmpnum//10
            tmp+=str(tmpnum)
        else: tmp+=s[i]
    if sum(list(map(int,tmp)))%10==0:print("T")
    else: print("F")