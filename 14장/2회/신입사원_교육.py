from heapq import heapify, heappush as push, heappop as pop

def solution(ability, number):
    heapify(ability)
    
    for i in range(number):
        a, b = pop(ability), pop(ability)
        push(ability, a + b)
        push(ability, a + b)
    
    return sum(ability)

