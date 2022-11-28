from itertools import permutations
import re

def toPostFix(tokens, priority):
    stack = []
    postfix = []
    
    for token in tokens:
        if token.isdigit(): postfix.append(token)
        else:
            if not stack: stack.append(token)
            else:
                while stack:
                    if priority[token] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    else: break
                    
                stack.append(token)
    
    while stack:
        postfix.append(stack.pop())
        
    return postfix

def calc(tokens):
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue

        num1 = stack.pop()
        num2 = stack.pop()
        if token == '*':
            stack.append(num2 * num1)
        elif token == '+':
            stack.append(num2 + num1)
        else:  # '-'
            stack.append(num2 - num1)

    return stack.pop()

def solution(expression):
    tokens = re.split(r'([-+*/()])|\s+', expression) 
    operators = ['+', '-', '*']
    answer = 0
    
    for i in map(list, permutations(operators)):
        #precedence and operator
        priority = {o:p for p, o in enumerate(list(i))}
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))

    return answer

