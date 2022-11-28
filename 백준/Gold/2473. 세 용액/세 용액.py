n = int(input())
solution = sorted(list(map(int,input().split())))

min_sol = 10 ** 9 * 3 - 2

for i in range(n-2):
    left = i + 1
    right = n - 1
    while left < right:
        multi = solution[i] + solution[left] + solution[right]
        if abs(multi) < min_sol:
            min_sol = abs(multi)
            answer = [solution[i], solution[left], solution[right]]
            
        if multi < 0:
            left += 1
        elif multi > 0:
            right -= 1
        else:
            break

print(*answer)
