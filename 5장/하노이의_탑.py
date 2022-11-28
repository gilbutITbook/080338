def hanoi(n, start, to, mid, answer):
    if n == 1:
        return answer.append([start, to])
    hanoi(n-1, start, mid, to, answer)
    answer.append([start, to])
    hanoi(n-1, mid, to, start, answer)
    
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

