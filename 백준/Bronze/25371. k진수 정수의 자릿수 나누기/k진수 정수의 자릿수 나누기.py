def convert(a, b) :
    base = ''
    while a > 0 :
        a, mod = divmod(a, b)
        base += str(mod)
    
    return base[::-1]
n, k = map(int, input().split())
nums = str(convert(n, k))
lst = []
tmp = ''
for i in nums :
    if i == '0' :	# '0'일 경우 tmp에 저장된 값을 lst에 저장 후 초기화
        lst.append(tmp)
        tmp = ''
        continue
    tmp += i
if len(tmp) > 0 :   # tmp 값에 값이 남아있을 경우 lst에 추가
    lst.append(tmp)

result = 0
for i in lst :
    if i.isdigit() :    # 문자의 숫자 판별
        result += int(i)
print(convert(result, k))