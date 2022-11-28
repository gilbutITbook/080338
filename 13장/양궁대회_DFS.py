def compare(current, before):
    for idx in range(10, 0, -1):
        if current[idx] > before[idx]: return True
        elif current[idx] < before[idx]: return False

def calc(lion, apeach):
    res = 0
    for i in range(len(lion)):
        if apeach[i] < lion[i]: res += 10 - i
        elif apeach[i] > lion[i]: res -= 10 - i
        
    return res

def dfs(info, idx, case, choose, n):
    if n < 0 or idx == 11: return

    if idx == 10 and n >= 0:
        current = [*choose, n]
        total = calc(current, info)
        if total > case[0]:
            case[0] = total
            case[1] = current
        elif total == case[0] and compare(current, case[1]): 
            case[1] = current

    dfs(info, idx+1, case, [*choose, info[idx] + 1], n - (info[idx] + 1))
    dfs(info, idx+1, case, [*choose, 0], n)

def solution(n, info):
    answer = [0, [0] * 11]
    
    dfs(info, 0, answer, [], n)
    return [-1] if not answer[0] else answer[1]

