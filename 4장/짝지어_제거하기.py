#실패하는 게 정상

def solution(s):
    while len(s) > 1:           
        s = list(s)              
        for i in range(len(s) - 1):    #배열 인덱스는 항상 신경 쓸 것
            if s[i] == s[i + 1]: s[i] = s[i + 1] = '' #중복 문자 공백으로 변경
        
        new_s = ''.join(s)             #문자열을 합치면서 공백 자동 제거
        if len(s) == len(new_s): break #변화가 없으면 제거하지 못했으므로 반복문 탈출
        s = new_s
    
    return 1 if len(s) == 0 else 0

