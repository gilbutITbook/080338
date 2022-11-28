def radixChange (num, radix):
    if num == 0: return '0'
    nums = []
    while num:
        num, rdx = divmod(num, radix)
        print(rdx)
        nums.append(str(rdx))
    return ''.join(reversed(nums))

def solution(n):
    return int(radixChange(n, 3)[::-1], 3)
