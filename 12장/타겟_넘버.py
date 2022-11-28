def dfs(numbers, step, total, target):    
    if step == len(numbers): return 1 if total == target else 0
    return dfs(numbers, step + 1, total + numbers[step], target) + dfs(numbers, step + 1, total - numbers[step], target)

def solution(numbers, target):
    return dfs(numbers, 0, 0, target)

