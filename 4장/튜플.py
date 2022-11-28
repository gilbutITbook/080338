def solution(s):
    data = s[2:-2].split("},{")
    data = sorted(data, key=lambda x: len(x))
    answer = []
    for item in data:
        item = list(map(int, item.split(",")))
        for value in item:
            if value not in answer:
                answer.append(value)
    return answer
