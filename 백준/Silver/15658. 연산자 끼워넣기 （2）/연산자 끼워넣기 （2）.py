n=int(input())
num = list(map(int,input().split()))
operater = list(map(int,input().split()))
max_num, min_num = -1e9, 1e9

def back(index, ans, plus, minus, mul, div):
  global max_num, min_num
  if index >= n:
    max_num = max(max_num, ans)
    min_num = min(min_num, ans)
    return
  if plus > 0:
    back(index+1, ans+num[index], plus-1, minus, mul, div)
  if minus > 0:
    back(index+1, ans-num[index], plus, minus-1, mul, div)
  if mul > 0:
    back(index+1, ans*num[index], plus, minus, mul-1, div)
  if div > 0:
    back(index+1, ans//num[index] if ans > 0 else -((-ans)//num[index]), plus, minus, mul, div-1)

back(1, num[0], operater[0], operater[1], operater[2], operater[3])
print(max_num)
print(min_num)