import sys
from collections import defaultdict
input = sys.stdin.readline

dic = defaultdict(int)
tree_num = 0
while True:
  s = input().rstrip()
  if not s:
    break
  tree_num += 1
  dic[s] += 1
sorted_dic = sorted(dic.items())
for i,j in sorted_dic:
  print("%s %.4f" %(i, (j/tree_num)*100))