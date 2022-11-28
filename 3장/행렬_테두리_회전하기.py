def solution(rows, columns, queries):
    grid = [[(i - 1) * columns + j for j in range(1, columns + 1)]
            for i in range(1, rows + 1)]
    answer = []

    for command in queries:
        x1, y1, x2, y2 = command
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        locations = []
        goods = []

        def construct_loc(x, y):
            nonlocal locations, goods, grid
            locations.append((x, y))
            goods.append(grid[x][y])

        for x in range(x1, x2):  # left top -> right top
            construct_loc(x, y1)
        for y in range(y1, y2):  # right top -> right bottom
            construct_loc(x2, y)
        for x in range(x2, x1, -1):  # right bottom -> left bottom
            construct_loc(x, y2)
        for y in range(y2, y1, -1):  # left bottom -> left top
            construct_loc(x1, y)

        answer.append(min(goods))
        lengoods = len(goods)
        for i in range(lengoods):
            x, y = locations[i]
            grid[x][y] = goods[(i + 1) % lengoods]

    return answer

def rotate(x1, y1, x2, y2, matrix):
    first = matrix[x1][y1]
    min_value = first
    
    # 왼쪽
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k+1][y1]
        min_value = min(min_value, matrix[k+1][y1])
    # 아래
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k+1]
        min_value = min(min_value, matrix[x2][k+1])
    # 오른쪽
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k-1][y2]
        min_value = min(min_value, matrix[k-1][y2])
    # 위
    for k in range(y2, y1+1, -1):
        matrix[x1][k] = matrix[x1][k-1]
        min_value = min(min_value, matrix[x1][k-1])
        
    matrix[x1][y1+1] = first
    return min_value

def solution(rows, columns, queries):
    matrix = [[(i)*columns+(j+1) for j in range(columns)] for i in range(rows)]
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(rotate(x1-1, y1-1, x2-1, y2-1, matrix))
        
    return result
