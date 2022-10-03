n = int(input())
st = []
dp = []
for i in range(n):
  a = int(input())
  st.append(a)
  dp.append(a)
dp[0] = st[0]
for i in range(1,n):
  for j in range(i):
    if st[i] > st[j]:
      dp[i] = max(dp[i], dp[j] + st[i])
print(max(dp))