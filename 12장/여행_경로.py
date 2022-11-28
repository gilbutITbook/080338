from collections import defaultdict

def dfs(graph, path, visit):
    if path:
        to = path[-1]
        if graph[to]: path.append(graph[to].pop(0))
        else: visit.append(path.pop())
        dfs(graph, path, visit)
        
    return visit[::-1]

def solution(tickets):
    graph = defaultdict(list)
    
    for a, b in tickets: graph[a].append(b)
    for key in graph.keys(): graph[key].sort()
    
    return dfs(graph, ["ICN"], [])

