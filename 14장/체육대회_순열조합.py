from itertools import combinations, permutations

def solution(ability):
    answer = 0
    people, event_size = len(ability), len(ability[0])
    scores = [i for i in range(people)]
    events = [i for i in range(event_size)]
    
    for i in combinations(scores, event_size):
        for j in permutations(events, event_size):
            power = 0 
            for k in range(len(j)): power += ability[i[k]][j[k]]
            answer = max(power, answer)
            
    return answer

