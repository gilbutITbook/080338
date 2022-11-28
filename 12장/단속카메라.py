def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001
    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

