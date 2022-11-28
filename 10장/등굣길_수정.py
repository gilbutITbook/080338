def dfs(y, x, dp, puddles):
    row, col = len(dp), len(dp[0])
    path = [[1,0], [0,1]]
    
    if [y, x] == [row-1, col-1]: return 1
    if dp[y][x] != 0: return dp[y][x]
    
    for i in range(2):
        ny = y + path[i][0]
        nx = x + path[i][1]

        if 0 <= ny < row and 0 <= nx < col:
            if [nx+1, ny+1] in puddles: continue
            dp[y][x] += dfs(ny, nx, dp, puddles)

    return dp[y][x] % 1000000007

def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    return dfs(0, 0, dp, puddles)

