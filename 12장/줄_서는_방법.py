from math import factorial

def solution(n, k):
    numbers = list(range(1, n + 1))
    answer = []
    k -= 1

    while numbers:
        idx, k = divmod(k, factorial(len(numbers) - 1))
        answer.append(numbers.pop(idx))
        
    return answer

