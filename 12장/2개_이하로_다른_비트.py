def f(x):
    if x % 2 == 0: return x + 1

    x = f'0{bin(x)[2:]}'
    x = f"{x[:x.rindex('0')]}10{x[x.rindex('0') + 2:]}"
    return int(x, 2)
        
def solution(numbers):
    return [f(number) for number in numbers]

