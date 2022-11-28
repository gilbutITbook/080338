from itertools import combinations
def solution(numbers):
    return sorted(set(map(sum, combinations(numbers, 2))))

