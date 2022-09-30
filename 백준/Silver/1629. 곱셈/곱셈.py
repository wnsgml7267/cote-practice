import sys
input = sys.stdin.readline
a, b, c = map(int,input().split())
def conquer(num, squared):
  if squared == 1:
    return num % c
  elif squared % 2 == 0:
    recursive = conquer(num, squared/2)
    return recursive * recursive % c
  else:
    recursive = conquer(num, (squared-1)/2)
    return recursive * recursive * num % c

print(conquer(a,b))