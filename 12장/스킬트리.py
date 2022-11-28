from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        skill_list = deque(skill[:])
        
        for s in skills:
            if s in skill and s != skill_list.popleft(): break
        else: answer += 1
        
    return answer

