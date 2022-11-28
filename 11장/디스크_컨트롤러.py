from heapq import heappush as push, heappop as pop

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                push(heap, job[::-1])
        
        if len(heap) > 0:
            cur = pop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
                
    return answer // len(jobs)

