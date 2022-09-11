from itertools import permutations
num = ['1','2','3','4','5','6','7','8','9']
array = list(permutations(num, 3))
n = int(input())
for _ in range(n):
  quiz, strike, ball = map(int,input().split())
  quiz = str(quiz)
  tmp = 0
  for i in range(len(array)):
    s = 0
    b = 0
    i -= tmp
    for j in range(3):
      if array[i][j] == quiz[j]:
        s += 1
      elif quiz[j] in array[i]:
        b += 1
    if strike != s or ball != b:
      array.remove(array[i])
      tmp += 1
print(len(array))
    