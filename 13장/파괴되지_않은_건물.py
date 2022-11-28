def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for attack_type, r1, c1, r2, c2, degree in skill:
        degree *= -1 if attack_type == 1 else 1
        temp[r1][c1] += degree
        temp[r1][c2 + 1] += -degree
        temp[r2 + 1][c1] += -degree
        temp[r2 + 1][c2 + 1] += degree

    for i in range(len(temp) - 1):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]

    for j in range(len(temp[0]) - 1):
        for i in range(len(temp) - 1):
            temp[i + 1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0: answer += 1

    return answer

