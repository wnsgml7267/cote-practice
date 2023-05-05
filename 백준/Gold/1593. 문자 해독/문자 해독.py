from collections import defaultdict as dd
import sys
input = sys.stdin.readline
W, S = map(int, input().split())
w = input().strip()
s = input().strip()
answer = 0
# w에 문자열마다 key설정 및 개수만큼 value값 증가
# s에서 w만큼 슬라이싱하여 key가 모두 존재하면 경우의 수 증가
w_arr = [0] * 58
s_arr = [0] * 58
idx = 0
for i in w:
  w_arr[ord(i) - 65] += 1
start = s[0]
for i in s[:W]:
  s_arr[ord(i)-65] += 1
if w_arr == s_arr:
  answer += 1
for i in range(W, S):
  s_arr[ord(s[i])-65] += 1
  s_arr[ord(s[i-W])-65] -= 1
  if w_arr == s_arr:
    answer += 1
print(answer)