def change(n, k):
    ret = []
    while n > 0:
        n, x = divmod(n, k)
        ret.append(str(x))
        
    return ''.join(ret[::-1])

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False

    return True

def solution(n, k):
    answer = 0
    k_num = change(n, k)
    
    for n in k_num.split('0'):
        if not n: continue
        if is_prime(int(n)): answer += 1
            
    return answer

