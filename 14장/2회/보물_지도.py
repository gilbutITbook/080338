from collections import deque

def solution(n, m, hole):
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dp = [[[-1, -1] for _ in range(m + 1)] for __ in range(n + 1)]
    dp[1][1][0] = 0

    mp = [[0] * (m + 1) for _ in range(n + 1)]
    for x, y in hole: mp[x][y] = 1

    q = deque()
    q.append((1, 1, 0))

    while q:
        x, y, b = q.popleft()

        for dx, dy in direction:
            for s in range(2):
                if b & s == 1: continue
                nx, ny, nb = x + dx * (s + 1), y + dy * (s + 1), b | s
                
                outside = nx < 1 or ny < 1 or nx > n or ny > m
                if outside or mp[nx][ny] > 0 or dp[nx][ny][nb] != -1: continue

                q.append((nx, ny, nb))
                dp[nx][ny][nb] = dp[x][y][b] + 1

    res = dp[n][m][1]
    if res == -1 or (dp[n][m][0] >= 0 and res > dp[n][m][0]): res = dp[n][m][0]

    return res

