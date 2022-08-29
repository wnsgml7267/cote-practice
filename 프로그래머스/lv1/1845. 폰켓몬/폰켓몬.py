def solution(nums):
    length, setnum = len(nums)//2, set(nums)
    if len(setnum) < length:
        length = len(setnum)
    return length