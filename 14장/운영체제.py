from heapq import heappush as push, heappop as pop

def push_task(waiting, tasks):
    start, priority, end = pop(tasks)
    push(waiting, (priority, start, end))
    return start

def solution(program):
    answer = [0 for _ in range(11)]
    tasks, waiting, curr = [], [], 0
    
    for p in program:
        push(tasks, (p[1], p[0], p[2]))
        
    while tasks or waiting:
        if not waiting: curr = push_task(waiting, tasks)

        priority, start, end = pop(waiting)
        answer[priority] += curr - start
        curr += end    
        
        while tasks and tasks[0][0] <= curr:
            push_task(waiting, tasks)
        
    answer[0] = curr
    return answer

