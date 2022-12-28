def solution(command):
    path = [[0, 1], [1, 0], [0, -1], [-1, 0]] 
    x = y = d = 0
    
    for i in command:
        if i == 'R': d = (d + 1) % 4
        elif i == 'L': d = (d + 3) % 4
        elif i == 'G':
            x += path[d][0]
            y += path[d][1]
        elif i == 'B':
            x -= path[d][0]
            y -= path[d][1]
            
    return [x,y]

