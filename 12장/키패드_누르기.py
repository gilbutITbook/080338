def dist(target, pos):
    return abs(target[0] - pos[0]) + abs(target[1] - pos[1])

def solution(numbers, hand):
    pattern = {'L': (1, 4, 7), 'R': (3, 6, 9)}
    pos = {'L': [0, 3], 'R': [2, 3]}
    result = []
    
    def press(which, coord):
        result.append(which)
        pos[which] = coord
    
    for number in numbers:
        choose = 'L'
        target = [0, (number - 1) // 3]
        
        if number in pattern['L']: pass
        elif number in pattern['R']: choose = 'R'
        else:
            target = [1, 3 if number == 0 else (number - 1) // 3]
            left = dist(target, pos['L'])
            right = dist(target, pos['R'])
            
            if right < left: choose = 'R'
            elif right == left and hand == 'right': choose = 'R'
        
        press(choose, target)
    
    return ''.join(result)

