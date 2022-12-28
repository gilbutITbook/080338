def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ': continue
        corr = ord('A') if s[i].isupper() else ord('a')
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)
            
    return ''.join(s)
