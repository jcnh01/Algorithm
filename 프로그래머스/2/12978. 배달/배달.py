import heapq
import sys

def solution(N, road, K):
    answer = 0
    heap = []
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road :
        graph[a].append((c, b))
        graph[b].append((c, a))
    heap.append((0, 1))
    dis = [sys.maxsize] * (N + 1)
    dis[1] = 0
    
    while heap :
        w, node = heapq.heappop(heap)
        if dis[node] != w : continue
        for next_w, next_node in graph[node] :
            if next_w + dis[node] < dis[next_node] :
                dis[next_node] = next_w + dis[node]
                heapq.heappush(heap, [dis[next_node], next_node])
                
    for i in range(1, N + 1) :
        if dis[i] <= K :
            answer += 1

    return answer