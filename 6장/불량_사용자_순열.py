from itertools import permutations
def solution(user_id, banned_id):
    banned = ' '.join(banned_id).replace('*','.')
    answer = set()
    
    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(banned, ' '.join(i)):
            answer.add(''.join(sorted(i)))
    
    return len(answer)
