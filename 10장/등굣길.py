#실패하는 게 정상

def dfs(y, x, row, col, puddles):
    path = [[1,0], [0,1]]
    answer = 0
    
    if [y, x] == [row-1, col-1]: return 1
    
    for i in range(2):
        ny = y + path[i][0]
        nx = x + path[i][1]

        if 0 <= ny < row and 0 <= nx < col:
            if [nx+1, ny+1] in puddles: continue
            answer += dfs(ny, nx, row, col, puddles)

    return answer % 1000000007

def solution(m, n, puddles):
    return dfs(0, 0, n, m, puddles)
