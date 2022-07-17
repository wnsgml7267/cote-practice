import sys
input = sys.stdin.readline
n = int(input())
str1 = str(input().strip())

dic = {}
result = [0,0]
start = 0
end = 0

while start < len(str1) and end < len(str1): #시작과 끝이 str1길이보다 작으면
  if str1[end] not in dic: #딕셔너리에 해당 인덱스 문자열 key에 value가 없다면
    dic[str1[end]] = 1
  else:
    dic[str1[end]] += 1 #있으면 += 1

  if len(dic) > n:  #알파벳 종류가 n개 보다 많아졌을 경우 start값을 올려 n개가 되도록 알파벳을 빼줌
    while start <= end and len(dic) > n:
      if dic[str1[start]] == 1:
        dic.pop(str1[start])
      else:
        dic[str1[start]] -= 1
      start += 1

  if len(dic) <= n: #연속된 n개의 문자열이 들어왔을경우 최대 길이로 갱신
    if result[1] - result[0] < end - start:
      result[0] = start
      result[1] = end
  end += 1
print(result[1] - result[0] + 1)
    