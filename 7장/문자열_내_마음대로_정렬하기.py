def solution(strings, n):
    '''이중 정렬'''
    return sorted(sorted(strings), key=lambda x: x[n])
    '''+ 추가'''
    return sorted(strings, key=lambda x: x[n]+x)
    '''튜플로 만들기'''
    return sorted(strings, key=lambda x: (x[n], x)) 

