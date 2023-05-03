t = int(input())
for i in range(t):
    k = int(input())    # 수강생 수
    d_nums = {}
    nums = list(map(int, input().split()))  # 수강생 참가번호
    n = int(input())    # 참가자 수
    best = 360
    for i in range(n):
        a, b, c = map(int, input().split())
        if a in nums:
            if b == -1:
                pass
            else:
                d_nums[a] = b * 60 + c
                if best > d_nums[a]:
                    best = d_nums[a]
    cnt = 0 # 인증서 받은 수강생 수
    b_nums = [] # 가장 기록이 좋은 수강생
    for key in d_nums.keys():
        if d_nums[key] == best:
            b_nums.append(key)
        if d_nums[key] != 0 and d_nums[key] <= 360:
            cnt += 1
    print(*b_nums, cnt)