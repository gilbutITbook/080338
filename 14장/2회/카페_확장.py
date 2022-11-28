from collections import deque

def solution(menu, order, k):
    queue = deque()
    busy = -1 
    idx = answer = 0

    for t in range(k * (len(order) - 1) + 1):
        if k * idx == t:
            queue.append(order[idx])
            idx += 1
        
        if busy == t:
            queue.popleft()
            busy = -1
        
        if busy == -1 and len(queue) > 0:
            busy = t + menu[queue[0]]
        
        answer = max(answer, len(queue))
    
    return answer

