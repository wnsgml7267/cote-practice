a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n = int(input())
s = input()
answer = 0
for idx, i in enumerate(s):
    answer += (31**idx) * (a.index(i)+1)
print(answer % 1234567891)
