def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y: return
    parent[x] = y

def find(parent, x):
    if parent[x] == x: return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def solution(n, costs):
    answer = cnt = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x:x[2])
    
    for i in range(len(costs)):
        if find(parent, costs[i][0]) != find(parent, costs[i][1]):
            union(parent, costs[i][0], costs[i][1])
            answer += costs[i][2]
            cnt += 1
        if cnt == n: break
    
    return answer

