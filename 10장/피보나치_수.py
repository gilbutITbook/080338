import sys
sys.setrecursionlimit(200000)

def fibo(n, answer):
    if n < 2: return 1
    if answer[n] == 0:
        answer[n] = fibo(n-1, answer) + fibo(n-2, answer) 
    
    return answer[n]

def solution(n):
    answer = [0] * (n)
    answer[0] = answer[1] = 1
    fibo(n - 1, answer)
    
    return answer[-1] % 1234567

