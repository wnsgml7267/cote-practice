vote = []
for i in range(int(input())):
  a = int(input())
  vote.append(a)
if len(vote) == 1:
  print(0)
else:
  president = vote[0]
  candidate = sorted(vote[1:], reverse=True)
  cnt = 0
  while (president <= candidate[0]):
    president += 1
    candidate[0] -= 1
    cnt += 1
    candidate = sorted(candidate, reverse=True)
  print(cnt)