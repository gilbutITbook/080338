from itertools import permutations
import re

def calc(tokens):
    num1, exp, num2 = tokens
    if exp == '+': return int(num1) + int(num2)
    elif exp == '*': return int(num1) * int(num2)
    else: return int(num1) - int(num2)

def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    for operator in permutations(operators):
        temp = re.split(r'([-+*/()])', expression)
        for exp in operator:
            while exp in temp:
                idx = temp.index(exp)
                temp[idx-1] = str(calc(temp[idx-1:idx+2]))
                temp[idx] = temp[idx + 1] = ''
                temp = [i for i in temp if i]
        answer.append(abs(int(temp[0])))
    return max(answer)

