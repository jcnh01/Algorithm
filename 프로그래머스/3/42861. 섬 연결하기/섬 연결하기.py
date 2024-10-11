import heapq

def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for a, b, c in costs :
        graph[a].append((c, b))
        graph[b].append((c, a))
        
    heap = []
    heap.append((0, 0))
    visit = [False] * (n + 1)
    
    while heap :
        w, node = heapq.heappop(heap)
        if not visit[node] :
            visit[node] = True
            answer += w
            for nw, next_node in graph[node] :
                if not visit[next_node] :
                    heapq.heappush(heap, (nw, next_node))
                
    return answer