def solution(genres, plays):
    answer = []

    info = {}
    gens = {}

    for idx, (gen, play) in enumerate(zip(genres, plays)):
        if gen not in info:
            info[gen] = [(idx, play)]
        else:
            info[gen].append((idx, play))
        
        gens[gen] = gens.get(gen, 0) + play

    for (gen, _) in sorted(gens.items(), key=lambda x:x[1], reverse=True):
        for (idx, _) in sorted(info[gen], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)

    return answer

