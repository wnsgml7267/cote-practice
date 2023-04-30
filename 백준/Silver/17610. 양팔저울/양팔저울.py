import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    sum_num = sum(arr) # 추의 합계

    before = [arr[0]]

    for i in range(1, n):
        now = [arr[i]]
        for j in before:
            now += [arr[i]+j, abs(arr[i] - j)]
        before += now
    before = list(set(before))
    if 0 in before:
        before.remove(0)
    print(sum_num - len(before))