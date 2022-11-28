from itertools import combinations_with_replacement as cwr

def solution(n, info):
    answer = [-1]
    max_gap = -1 

    for shot in cwr(range(11), n):
        case = [0] * 11
        for i in shot: case[10 - i] += 1

        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == case[idx] == 0: continue
            elif info[idx] >= case[idx]: apeach += 10 - idx
            else: lion += 10 - idx

        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = case
                
    return answer

