def solution(s):
    stack = []
    for case in s:
        if stack and stack[-1] == case: stack.pop() #스택에 값이 있고 마지막이 같은지
        else: stack.append(case)
    return 0 if stack else 1

