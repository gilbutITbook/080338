def solution(s):
    answer = {} #배열([])에서 딕셔너리({})로 교체
    s = sorted(s[2:-2].split("},{"), key=len)
    for tuples in s:
        elements = tuples.split(',')
        for element in elements:
            number = int(element)
            if number not in answer:
                answer[number] = 1 #딕셔너리 키를 사용 (값value은 아무거나)
                
    return list(answer) #딕셔너리의 키 값만 배열의 인자가 됨
