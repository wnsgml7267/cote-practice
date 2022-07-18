import sys
input = sys.stdin.readline

def solve(l, s): #문자열 길이, 추가할 알파벳
  if l == 0: #문자열 길이만큼 모두 사용했으면, 알파벳(s)을 visited에 추가
    visited.add(s)
    return
  for i in range(26):
    if alpha[i] >= 1: #존재하는 알파벳이면 문자열 길이를 감소시키고, s에 해당 알파벳 더하여 재귀
      alpha[i] -= 1
      solve(l-1, s+chr(i+97))
      alpha[i] += 1
      
for i in range(int(input())):
  s = input().rstrip()
  visited = set()
  alpha = [0 for _ in range(26)]

  for i in s:
    alpha[ord(i)-97] += 1

  solve(len(s), '')
  for s in sorted(list(visited)):
    print(s)