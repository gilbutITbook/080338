def solution(N, number):
    dp = [set() for i in range(9)] 
    for i in range(1, 9):
        case = dp[i]
        case.add(int(str(N) * i))
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    case.add(k + l) 
                    case.add(k - l)
                    case.add(k * l)
                    if l != 0 and k != 0: case.add(k // l) 

        if number in case: return i
    return -1

