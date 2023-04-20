n = int(input())
s = input()
score = 0
bonus = 0
for i in range(len(s)):
    if s[i] == 'O':
        score += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0
print(score)