def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    result = ''.join(numbers)
    if '0' * len(numbers) == result: return '0'
    return result

