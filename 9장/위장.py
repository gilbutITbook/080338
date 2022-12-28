def solution(clothes):
    answer = 1
    cloth_type = {}
    for cloth, type in clothes:
        cloth_type[type] = cloth_type.get(type, 0) + 1
        
    for type in cloth_type:
        answer *= (cloth_type[type] + 1)

    return answer - 1

