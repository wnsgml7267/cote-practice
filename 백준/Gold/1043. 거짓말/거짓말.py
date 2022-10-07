n, m = map(int,input().split())
true_array = set(input().split()[1:])
parties = []

for _ in range(m):
  parties.append(set(input().split()[1:]))

for _ in range(m): #파티 수 만큼 반복
  for party in parties:
    if party & true_array: #진실을 아는 사람이 있다면
      true_array = true_array.union(party) #그 파티에 있는 모든 사람은 진실을 아는 사람이 됨
cnt = 0
for party in parties:
  if party & true_array:
    continue
  cnt += 1
print(cnt)
