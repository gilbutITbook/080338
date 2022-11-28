def collatz(num, answer):
    if num == 1: return answer 
    if answer == 500: return - 1 
        
    if num % 2 == 0:
        return collatz(num // 2, answer+1)
    elif num % 2 == 1:
        return collatz(num * 3 + 1, answer+1)

def solution(num):
    return collatz(num, 0)
