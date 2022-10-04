n=int(input())
p=int(input())

array = [500, 0.9, 2000, 0.75]
answer = p
r = n//5
if r > 4:
  r=4
for i in range(r):
  if i == 0 or i == 2:
    answer = min(answer, p - array[i])

  else:
    answer = min(answer, int(p*array[i]))

if answer < 0:
  print(0)
else:
  print(answer)