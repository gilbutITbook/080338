def solution(line):
    meet = list()
    x_max = y_max = -float('inf')
    x_min = y_min = float('inf')
    
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if ((a * d) - (b * c)) == 0:
                continue
                
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                meet.append([x, y])
                x_max, y_max = max(x_max, x), max(y_max, y)
                x_min, y_min = min(x_min, x), min(y_min, y)
                
    meet = sorted(meet, key = lambda i: -i[1])
    width = abs(x_max - x_min) + 1
    height = abs(y_max - y_min) + 1
    answer = [['.'] * width for _ in range(height)]
    
    for x, y in meet:
        ny = y_max - y
        nx = x - x_min
        answer[ny][nx] = '*'

    return list(map(''.join, answer))
