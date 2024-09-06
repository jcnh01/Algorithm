from collections import deque

q = deque()

def bfs(graph, visit, distance) :
    while q :
        num, d = q.popleft()
        distance[num] = d
        for g in graph[num] :
            if not visit[g] :
                q.append((g, d + 1))
                visit[g] = True
        
def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visit = [False] * (n+1)
    distance = [0] * (n+1)
    
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    q.append((1, 0))
    
    bfs(graph, visit, distance)
    
    distance[1] = 0
    for d in distance :
        if max(distance) == d :
            answer += 1
    
    return answer