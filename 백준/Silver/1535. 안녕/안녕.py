n = int(input())
hp = list(map(int,input().split()))
happy = list(map(int,input().split()))
dp = [0]*101
for i in range(n):
  damage = hp[i]
  get_happy = happy[i]
  for j in range(100, 0, -1):
    if j > damage: #체력이 깎여도 죽지 않을 때
      dp[j] = max(dp[j], dp[j-damage]+get_happy) #사람을 만나지 않았을 때, 만났을 때 비교
print(dp[-1])