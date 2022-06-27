import sys
input = sys.stdin.readline
S = input().rstrip()
T = input().rstrip()
count = 0
def solve(T):
  global count
  if len(S) < len(T):
    if T[0] == "B" and T[-1] == "A":
      solve((T[::-1])[:-1])
      solve(T[:-1])
    else:
      if T[0] == "B":
        solve((T[::-1])[:-1])
      elif T[-1] == "A":
        solve(T[:-1])  
      else :
        count += 0
      
  if len(S) == len(T):
    if S == T:
      count += 1
solve(T)
if count > 0:
  print(1)
else:
  print(0)

  