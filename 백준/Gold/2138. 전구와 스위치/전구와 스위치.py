n = int(input())
switch = list(map(int,input()))
target = list(map(int,input()))

def change(a,b):
  l = a[:]
  cnt = 0
  for i in range(1,n): #전구 1~n
    if l[i-1] == b[i-1]: #이전 전구가 같으면 continue
      continue
    cnt += 1 #전구가 다르면 +1
    for j in range(i-1, i+2):
      if j<n:
        l[j] = 1 - l[j] #스위치 변경
  return cnt if l == b else 1e9
ans = change(switch, target) #첫 전구 스위치 안눌렀을 때
#첫 전구 스위치 눌렀을 때
switch[0] = 1 - switch[0]
switch[1] = 1 - switch[1]
ans = min(ans, change(switch, target)+1)
print(ans if ans != 1e9 else -1)