def check(string):
    stack = []
    
    for bracket in string:
        if bracket == '(': stack.append('(')
        elif stack: stack.pop()
        else: return False
    
    return True
 
def dfs(string):
    if not string: return string #1
    close = 0

    for i in range(len(string)):
        if string[i] == '(': close += 1
        else: close -= 1

        if close == 0:  #2
            if check(string[:i + 1]): #3
                return ''.join([string[:i + 1], *dfs(string[i + 1:])]) #3-1
            else: #4
                v = ['(', *dfs(string[i + 1:]), ')'] #4-1, 4-2, 4-3
                for a in range(1, i): #4-4
                    if string[a] == '(': v.append(')')
                    else: v.append('(')
                    
                return ''.join(v) #4-5
               
def solution(p):
    return dfs(p)

