def solution(info, query):
    data = [i.split() for i in info]
    queries = []
    
    for q in query:
        q = q.split()
        for _ in range(3): q.remove('and')
        queries.append(q)
        
    answer = [0] * len(query)
    
    for i in range(len(queries)):
        q = queries[i]
        for info in data:
            for j in range(5):
                if q[j] == '-': continue
                elif j == 4 and int(info[j]) >= int(q[j]): answer[i] += 1
                elif info[j] != q[j]: break
            
    return answer

