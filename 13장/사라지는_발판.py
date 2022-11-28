def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    inside = lambda x, y: 0 <= x < n and 0 <= y < m

    def dfs(aloc, bloc, seen, step):
        x, y = aloc if step % 2 == 0 else bloc
        survive, must_lose = False, True
        win_left, lose_left = [], []
        
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            
            if inside(nx, ny) and (nx, ny) not in seen and board[nx][ny]:
                survive = True
                if aloc == bloc: return (True, step + 1)
            
                next_step = [[nx, ny], bloc] if step % 2 == 0 else [aloc, [nx, ny]]
                win, left = dfs(*next_step, seen | {(x, y)}, step + 1)
                
                if win: win_left.append(left)
                else: lose_left.append(left)
                must_lose &= win
                
        if not survive: return (False, step)
        if must_lose: return (False, max(win_left))
        return (True, min(lose_left))

    return dfs(aloc, bloc, set(), 0)[1]

