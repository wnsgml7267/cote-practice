import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = list(input().rstrip())
str1_len, str2_len = len(str1), len(str2)
dp = [0] * str2_len

for i in range(str1_len):
    count = 0
    for j in range(str2_len):
        if count < dp[j]: # 더 큰 긴 부분 문자열이 있다면
            count = dp[j]
        elif str1[i] == str2[j]:
            dp[j] = count + 1
print(max(dp))