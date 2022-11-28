def back(gen, x):
    child = ["RR", "Rr", "Rr", "rr"]
    if gen == 1: return "Rr"

    parent = back(gen - 1, x // 4)
    if parent == "Rr": return child[x % 4]
    else: return parent

def solution(queries):
    answer = []

    for query in queries:
        n, p = query
        result = back(n, p - 1)
        answer.append(result)
        
    return answer

