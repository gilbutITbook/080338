from collections import deque

def solution(board):
    size = len(board)
    paths = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    def bfs(x, y, cost, path): 
        graph = [[0] * size for _ in range(size)]
        for a in range(size):
            for b in range(size):
                if board[a][b] == 1: graph[a][b] = -1
                
        q = deque()
        q.append((x, y, cost, path))
        
        while q:
            x, y, cost, path = q.popleft()
            
            for i in range(len(paths)):
                nx = x + paths[i][0]
                ny = y + paths[i][1]
                
                if nx < 0 or nx >= size or ny < 0 or ny >= size or graph[nx][ny] == -1: continue

                if path == i: newcost = cost + 100
                else: newcost = cost + 600
                
                if graph[nx][ny] == 0 or (graph[nx][ny] != 0 and graph[nx][ny] > newcost):
                    q.append((nx, ny, newcost, i))
                    graph[nx][ny] = newcost

        return graph[size - 1][size - 1]

    return min(bfs(0, 0, 0, 2), bfs(0, 0, 0, 3))

