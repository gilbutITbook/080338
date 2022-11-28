def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {uid: 0 for uid in id_list}
    
    for r in set(report):
        reports[r.split()[1]] += 1
        
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

