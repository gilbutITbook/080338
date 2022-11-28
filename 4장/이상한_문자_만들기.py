def solution(s):
    s = list(s)
    cnt = 0
    
    for i in range(len(s)):
        if s[i] == ' ': 
            cnt = 0
            continue
            
        s[i] = s[i].upper() if cnt % 2 == 0 else s[i].lower()
        cnt += 1
    
    return ''.join(s)
