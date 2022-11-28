from collections import defaultdict

def solution(info, edges):
    answer = []
    graph = defaultdict(list)
    for parent, child in edges: graph[parent].append(child)
    
    def dfs(current, sheep, wolf, possible_path):
        sheep += info[current] ^ 1
        wolf += info[current]

        if sheep <= wolf: return
        if sheep > wolf:
            answer.append(sheep)
            for upcoming in possible_path:
                temp = set(graph.get(upcoming, []))
                possible_path |= temp
                possible_path -= set([upcoming])
                dfs(upcoming, sheep, wolf, possible_path)
                possible_path |= set([upcoming])
                possible_path -= temp
                
    dfs(0, 0, 0, set(graph.get(0)))
    return max(answer)

