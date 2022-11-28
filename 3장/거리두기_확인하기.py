def check(place):
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            if cell != 'P':
                continue
            
            isNotEndRow = idx_row != 4
            isNotEndCol = idx_col != 4
            isNotFirstCol = idx_col != 0
            isBeforeThirdRow = idx_row < 3
            isBeforeThirdCol = idx_col < 3
            
            #D(Down), D2(2 times Down)
            #R(Right), R2(2 times Right)
            #L(Left)
            #RD(Right-Down), LD(Left-Down)

            if isNotEndRow:
                D = place[idx_row + 1][idx_col]
                if D == 'P': return 0
                if isBeforeThirdRow:
                    D2 = place[idx_row + 2][idx_col]
                    if D2 == 'P' and D != 'X': return 0
                if isNotEndCol:
                    R = place[idx_row][idx_col + 1]
                    RD = place[idx_row + 1][idx_col + 1]
                    if RD == 'P' and (D != 'X' or R != 'X'): return 0
                if isNotFirstCol:
                    L = place[idx_row][idx_col - 1]
                    LD = place[idx_row + 1][idx_col - 1]
                    if LD == 'P' and (D != 'X' or L != 'X'): return 0
            if isNotEndCol:
                R = place[idx_row][idx_col + 1]
                if R == 'P': return 0
                if isBeforeThirdCol:
                    R2 = place[idx_row][idx_col + 2]
                    if R2 == 'P' and R != 'X': return 0
                
    return 1

def solution(places):
    return [check(place) for place in places]
