import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]

for _ in range(e) :
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visit = [False] * (v + 1)

heap = [(0, 1)]
rs = 0

while heap :
    w, node = heapq.heappop(heap)
    if not visit[node] :
        visit[node] = True
        rs += w
        for next_node in graph[node] :
            if not visit[next_node[1]] :
                heapq.heappush(heap, next_node)

print(rs)