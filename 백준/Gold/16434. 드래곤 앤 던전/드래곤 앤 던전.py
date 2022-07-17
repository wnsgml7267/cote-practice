import sys
input = sys.stdin.readline
room_count, attack = map(int,input().split()) #방 개수, 공격력
ans = []
cur_hp=0
h_hp=0

for i in range(room_count):
  t, a, h = map(int,input().split())
  damage=0
  if t == 1: #a=몬스터 공격력, h=몬스터 체력
    if h % attack == 0:
      damage += -(a*(h//attack-1))
    else:
      damage += -(a*(h//attack))
    ans.append(damage)
  elif t == 2: #a=용사 공격력 증가, h=용사 체력회복
    attack += a
    damage = h
  cur_hp += damage
  if cur_hp > 0:
    cur_hp=0
  h_hp = max(h_hp,abs(cur_hp))
print(h_hp+1)
      
