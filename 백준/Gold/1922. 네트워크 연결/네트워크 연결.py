import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(e) :
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

import heapq
heap = []
heap.append((0, 1))
visit = [False] * (v + 1)

rs = 0

while heap :
    w, node = heapq.heappop(heap)
    if not visit[node] :
        rs += w
        visit[node] = True
        for next_node in graph[node] :
            if not visit[next_node[1]] :
                heapq.heappush(heap, next_node)

print(rs)