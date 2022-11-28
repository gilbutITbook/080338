def solution(brown, yellow):
    grid = brown + yellow
    for n in range(3, int(grid ** 0.5) + 1):
        if grid % n != 0: continue
        m = grid // n
        if (n-2) * (m-2) == yellow:
            return [m, n]

