def solution(gems):
    kind = len(set(gems))
    size = len(gems)
    answer = [0, size - 1]
    
    dic = {gems[0]:1}
    start = end = 0
    
    while end < size:
        if len(dic) < kind:
            end += 1
            if end == size: break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
        else:
            if (end - start + 1) < (answer[1] - answer[0] + 1): answer = [start, end]
            if dic[gems[start]] == 1: del dic[gems[start]]
            else: dic[gems[start]] -= 1
            start += 1

    answer[0] += 1
    answer[1] += 1
    
    return answer

