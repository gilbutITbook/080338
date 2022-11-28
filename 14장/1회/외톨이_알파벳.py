def solution(input_string): 
    d = {}
    prev = None
    
    for x in input_string:
        if x in d and prev != x: d[x] = True
        elif x not in d: d[x] = False
        prev = x
    
    answer = [k if d[k] else '' for k in d]
    return ''.join(sorted(answer)) or 'N'

