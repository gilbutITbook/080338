def solution(n, results):
    total = [['????' for i in range(n)] for j in range(n)]

    for i in range(n):
        total[i][i] = 'SELF'

    for result in results:
        total[result[0] - 1][result[1] - 1] = 'WINS'
        total[result[1] - 1][result[0] - 1] = 'LOSE'
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WINS' and total[k][j] == 'WINS':
                    total[i][j] = 'WINS'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'

    answer = 0

    for i in total:
        if '????' not in i:
            answer += 1

    return answer

